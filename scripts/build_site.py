from __future__ import annotations

import html
import posixpath
import re
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = "https://cadur.github.io/codex-seo"


def read_skill(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", text, re.S)
    if not frontmatter:
        raise ValueError(f"Missing SKILL.md frontmatter: {path}")
    metadata, body = frontmatter.groups()
    fields = {key: value.strip().strip('"\'') for key, value in re.findall(r"^(name|description):\s*(.+)$", metadata, re.M)}
    if not fields.get("name") or not fields.get("description"):
        raise ValueError(f"Skill needs name and description: {path}")
    title = next((line.lstrip("# ").strip() for line in body.splitlines() if line.startswith("# ")), fields["name"].replace("-", " ").title())
    return {**fields, "title": title, "body": body.strip(), "slug": fields["name"]}


def markdown(source: str, skill_slug: str = "") -> str:
    out, paragraph, listing, code = [], [], None, False

    def inline(text: str) -> str:
        text = html.escape(text)
        codes = []

        def save_code(match: re.Match[str]) -> str:
            codes.append("<code>" + match.group(1) + "</code>")
            return f"\x00{len(codes) - 1}\x00"

        text = re.sub(r"`([^`]+)`", save_code, text)
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

        def link(match: re.Match[str]) -> str:
            label, escaped_url = match.groups()
            url = html.unescape(escaped_url)
            parts = urlsplit(url)
            if not parts.scheme and url.startswith("/") and not url.startswith("//"):
                url = "/codex-seo" + url
            elif not parts.scheme and not url.startswith("#"):
                repo_path = posixpath.normpath(posixpath.join("skills", skill_slug, url))
                if repo_path.startswith("docs/"):
                    url = "/codex-seo/" + repo_path.removeprefix("docs/")
                else:
                    url = "https://github.com/CaduR/codex-seo/blob/main/" + quote(repo_path, safe="/")
                parts = urlsplit(url)
            safe = parts.scheme in {"http", "https", "mailto"} or url.startswith("/codex-seo/") or url.startswith("#")
            if not safe:
                return label
            href = html.escape(url, quote=True)
            external = parts.scheme in {"http", "https"}
            attrs = ' target="_blank" rel="noopener noreferrer"' if external else ""
            return f'<a href="{href}"{attrs}>{label}</a>'

        text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", link, text)
        for index, value in enumerate(codes):
            text = text.replace(f"\x00{index}\x00", value)
        return text

    def table_cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    def is_table_rule(line: str) -> bool:
        cells = table_cells(line)
        return len(cells) > 1 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)

    def flush_paragraph() -> None:
        if paragraph:
            out.append("<p>" + inline(" ".join(part.strip() for part in paragraph)) + "</p>")
            paragraph.clear()

    def flush_list() -> None:
        nonlocal listing
        if listing:
            out.append(f"</{listing}>")
            listing = None

    lines = source.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            flush_paragraph(); flush_list()
            out.append("<pre><code>" if not code else "</code></pre>")
            code = not code
        elif code:
            out.append(html.escape(line) + "\n")
        elif not line.strip():
            flush_paragraph(); flush_list()
        elif line.startswith(">"):
            flush_paragraph(); flush_list()
            quoted = []
            while index < len(lines) and lines[index].startswith(">"):
                quoted.append(lines[index].lstrip("> "))
                index += 1
            out.append("<blockquote><p>" + inline(" ".join(quoted)) + "</p></blockquote>")
            continue
        elif index + 1 < len(lines) and "|" in line and is_table_rule(lines[index + 1]):
            flush_paragraph(); flush_list()
            headers = table_cells(line)
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(cell)}</th>" for cell in headers) + "</tr></thead><tbody>")
            index += 2
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                cells = table_cells(lines[index])
                cells += [""] * max(0, len(headers) - len(cells))
                out.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells[:len(headers)]) + "</tr>")
                index += 1
            out.append("</tbody></table>")
            continue
        elif re.fullmatch(r"\s*(?:---+|\*\*\*+|___+)\s*", line):
            flush_paragraph(); flush_list()
            out.append("<hr>")
        elif line.startswith("#"):
            flush_paragraph(); flush_list()
            level = min(len(line) - len(line.lstrip("#")), 4)
            out.append(f"<h{level}>{inline(line[level:].strip())}</h{level}>")
        elif re.match(r"\s*[-*+]\s+", line) or re.match(r"\s*\d+[.)]\s+", line):
            flush_paragraph()
            ordered = bool(re.match(r"\s*\d+[.)]\s+", line))
            wanted = "ol" if ordered else "ul"
            if listing != wanted:
                flush_list(); listing = wanted; out.append(f"<{listing}>")
            item = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
            out.append(f"<li>{inline(item)}</li>")
        else:
            if listing and line[:1].isspace() and out and out[-1].endswith("</li>"):
                out[-1] = out[-1][:-5] + " " + inline(line.strip()) + "</li>"
                index += 1
                continue
            flush_list()
            paragraph.append(line)
        index += 1
    flush_paragraph(); flush_list()
    if code:
        out.append("</code></pre>")
    return "\n".join(out)


def page(title: str, description: str, content: str, canonical: str, extra_head: str = "") -> str:
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#111111"><meta name="description" content="{html.escape(description, quote=True)}"><link rel="canonical" href="{canonical}"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title, quote=True)} | Codex SEO"><meta property="og:description" content="{html.escape(description, quote=True)}">{extra_head}<title>{html.escape(title)} | Codex SEO</title><link rel="stylesheet" href="/codex-seo/assets/site.css"></head><body>{content}</body></html>'''


def build() -> None:
    skills = [read_skill(path) for path in sorted((ROOT / "skills").glob("*/SKILL.md"))]
    if len(skills) != 26 or len({skill["slug"] for skill in skills}) != 26:
        raise SystemExit(f"Expected 26 unique skills; found {len(skills)}")
    skills_dir = DOCS / "skills"
    for old in skills_dir.glob("*/index.html") if skills_dir.exists() else []:
        old.unlink()
    skills_dir.mkdir(parents=True, exist_ok=True)
    cards = []
    for i, skill in enumerate(skills, 1):
        slug, title, desc = skill["slug"], skill["title"], skill["description"]
        cards.append(f'''<a class="skill-card" href="skills/{html.escape(slug)}/" data-search="{html.escape((slug + ' ' + title + ' ' + desc).lower(), quote=True)}"><span class="card-no">{i:02}</span><span class="card-title">{html.escape(title)}</span><span class="card-desc">{html.escape(desc)}</span><span class="card-link">Explorar workflow <b>↗</b></span></a>''')
        detail = f'''<header class="top"><a class="brand" href="/codex-seo/"><span class="brand-mark">C</span> CODEX <b>SEO</b></a><nav><a href="/codex-seo/#catalogo">CATÁLOGO</a><a href="/codex-seo/#instalar">INSTALAÇÃO</a><a href="https://github.com/CaduR/codex-seo">GITHUB ↗</a></nav></header><main><div class="detail-hero"><a class="crumb" href="/codex-seo/#catalogo">← TODAS AS SKILLS</a><span class="eyebrow">WORKFLOW {i:02} / 26</span><h1>{html.escape(title)}</h1><p class="lead">{html.escape(desc)}</p><div class="detail-tags"><span>SKILL CODEX</span><span>OPEN SOURCE · MIT</span><span>SEM API PAGA OBRIGATÓRIA</span></div></div><section class="detail-grid"><div class="detail-main"><div class="section-kicker">// COMO USAR</div><h2>Workflow no Codex</h2><p>Peça ao Codex para usar <code>${html.escape(slug)}</code> com a URL, página, assunto ou conjunto de dados relevante. Veja as ferramentas expostas e dependências desta skill no <a href="/codex-seo/CAPABILITY-MAP.md">mapa de capacidades</a>.</p><article class="workflow">{markdown(skill["body"], slug)}</article></div><aside class="detail-aside"><div class="section-kicker">// LIMITES</div><h3>O que esperar</h3><p>As recomendações devem ser ligadas a evidências observadas. Se uma página, conta ou fonte de dados não estiver acessível, o resultado precisa indicar essa limitação.</p><p>Dados do Google, backlinks, posições e buscas atuais não são presumidos. Conexões de terceiros podem exigir conta, permissão e custos próprios.</p><a class="button button-orange" href="/codex-seo/#instalar">INSTALAR O CODEX SEO ↗</a></aside></section><section class="next"><span class="section-kicker">// CONTINUE</span><h2>Explore as outras skills</h2><a href="/codex-seo/#catalogo">Voltar ao catálogo →</a></section></main><footer><span>CODEX SEO · MIT LICENSE</span><a href="https://github.com/CaduR/codex-seo">GITHUB ↗</a></footer>'''
        (skills_dir / slug).mkdir(exist_ok=True)
        (skills_dir / slug / "index.html").write_text(page(title, desc, detail, f"{BASE}/skills/{slug}/"), encoding="utf-8")

    content = f'''<a class="skip" href="#main">Pular para o conteúdo</a><header class="top"><a class="brand" href="#top"><span class="brand-mark">C</span> CODEX <b>SEO</b></a><nav><a href="#recursos">RECURSOS</a><a href="#catalogo">SKILLS</a><a href="#instalar">INSTALAR</a><a href="https://github.com/CaduR/codex-seo">GITHUB ↗</a></nav></header><main id="main"><section id="top" class="hero"><div class="hero-copy"><span class="eyebrow">// 26 SKILLS · OPEN SOURCE · MIT</span><h1>SEU TIME DE SEO.<br><span>NO CODEX.</span></h1><p class="hero-lead">Workflows para analisar SEO técnico, conteúdo, dados estruturados, busca local e muito mais — direto no Codex.</p><p class="hero-detail">Skills Codex adaptadas do catálogo Claude SEO. Cada uma explica o processo, os limites das evidências e quando uma integração externa é necessária.</p><div class="install-line"><span>$</span><code>codex plugin marketplace add CaduR/codex-seo</code><button class="copy" type="button" aria-label="Copiar comando">COPIAR</button></div><div class="hero-links"><span>GRÁTIS · LICENÇA MIT</span><a href="#catalogo">EXPLORAR AS SKILLS ↓</a></div></div><div class="hero-art" aria-label="Visão abstrata de um fluxo de SEO"><div class="orb orb-one"></div><div class="orb orb-two"></div><div class="hero-ring"></div><div class="hero-window"><div class="window-top"><i></i><i></i><i></i><span>SEO / AUDIT</span></div><div class="window-line wide"></div><div class="window-line"></div><div class="window-score"><strong>26</strong><span>WORKFLOWS<br>NO CODEX</span></div><div class="window-bars"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div><span class="art-label label-one">TECHNICAL</span><span class="art-label label-two">CONTENT</span><span class="art-label label-three">SEARCH</span></div></section><section class="metrics" aria-label="Resumo"><div><strong>26</strong><span>SKILLS</span></div><div><strong>19</strong><span>PAPÉIS ESPECIALISTAS</span></div><div><strong>63</strong><span>SCRIPTS PORTADOS</span></div><div><strong>$0</strong><span>APIs PAGAS OBRIGATÓRIAS</span></div><p>O servidor MCP padrão expõe análises locais e de leitura; integrações pagas exigem configuração externa.</p></section><section id="recursos" class="features"><div class="section-heading"><span class="eyebrow">// O QUE COBRE</span><h2>Do crawl à experiência<br>de busca.</h2><p>Fluxos especializados ajudam o Codex a revisar sinais concretos e organizar recomendações acionáveis.</p></div><div class="feature-grid"><article><span>01 / VISIBILIDADE</span><h3>SEO técnico</h3><p>Rastreabilidade, indexação, canonicals, schema, sitemaps e experiência mobile.</p></article><article><span>02 / CONTEÚDO</span><h3>Conteúdo útil</h3><p>E-E-A-T, briefs, estrutura editorial, clusters temáticos e páginas comparativas.</p></article><article><span>03 / DESCOBERTA</span><h3>Busca que muda</h3><p>GEO, SEO local, internacional, e-commerce e prontidão para agentes.</p></article><article><span>04 / EVIDÊNCIA</span><h3>Dados com contexto</h3><p>Google, backlinks e SERPs entram apenas quando as ferramentas autorizadas estão conectadas.</p></article></div></section><section id="catalogo" class="catalog"><div class="section-heading catalog-heading"><div><span class="eyebrow">// TODAS AS SKILLS</span><h2>Escolha seu workflow.</h2></div><label class="search-label"><span>BUSCAR</span><input id="search" type="search" placeholder="SEO técnico, conteúdo…" autocomplete="off"></label></div><div class="skill-grid">{"".join(cards)}</div><p id="empty" class="empty" hidden>Nenhuma skill encontrada.</p></section><section class="scoring"><div><span class="eyebrow">// EVIDÊNCIA ANTES DE OPINIÃO</span><h2>Sem promessas<br>de ranking.</h2><p>As skills organizam achados e recomendações a partir do que o Codex consegue verificar. Um score heurístico pode servir para triagem, nunca como métrica oficial do Google ou garantia de resultado.</p></div><div class="score-card"><div class="score-head"><span>PRIORIDADE DOS ACHADOS</span><span>REVISÁVEL</span></div><div class="score-row"><b>CRÍTICO</b><i class="bar critical"></i><span>Bloqueia acesso ou indexação</span></div><div class="score-row"><b>ALTO</b><i class="bar high"></i><span>Risco claro para usuários ou busca</span></div><div class="score-row"><b>MÉDIO</b><i class="bar medium"></i><span>Oportunidade bem sustentada</span></div><div class="score-row"><b>BAIXO</b><i class="bar low"></i><span>Ajuste incremental</span></div></div></section><section class="faq"><div class="section-heading"><span class="eyebrow">// FAQ</span><h2>Perguntas diretas.</h2></div><div class="faq-list"><details><summary>É idêntico ao Claude SEO?</summary><p>Reproduz as 26 áreas de workflow e os principais materiais de referência, adaptados ao Codex. A interface de comandos, runtime e integrações específicas do Claude não são iguais: o Codex usa skills e um servidor MCP local. A paridade com APIs de terceiros depende de conexões autorizadas.</p></details><details><summary>O plugin rastreia sites inteiros?</summary><p>O MCP oferece a ferramenta <code>seo_crawl</code> para auditorias Lighthouse de até 50 rotas, quando solicitada explicitamente. Requer Node.js 18+ e baixa o runner fixado na primeira execução. Sites muito grandes continuam exigindo inventário e rastreamento dedicados.</p></details><details><summary>As 19 funções de especialista são agentes instaláveis?</summary><p>São cartões de papel para guiar análises delegadas ou inline. A delegação paralela depende das ferramentas que a sessão Codex disponibilizar; o pacote não instala 19 agentes independentes.</p></details><details><summary>Precisa pagar por API?</summary><p>Não. Nenhuma API paga é obrigatória. DataForSEO pode ser conectado separadamente por OAuth no Codex; outros provedores precisam de uma conexão MCP compatível. Consulte o guia de <a href="/codex-seo/EXTENSIONS.md">extensões</a>.</p></details><details><summary>O que o setup instala?</summary><p>Pacotes Python open source em um ambiente isolado na pasta de dados do usuário. Chromium é opcional. O setup não conecta contas SEO nem envia dados de analytics.</p></details></div></section><section id="instalar" class="install"><div><span class="eyebrow">// COMECE AGORA</span><h2>Instale no Codex.</h2><p>Adicione o marketplace e instale Codex SEO pela área de plugins do aplicativo.</p></div><div class="install-steps"><div><b>01</b><code>codex plugin marketplace add CaduR/codex-seo</code></div><div><b>02</b><span>Abra Plugins no Codex e instale <strong>Codex SEO</strong>.</span></div><div><b>03</b><span>Inicie um workflow, por exemplo <code>$seo-audit https://seusite.com</code>.</span></div></div></section><section class="about"><span class="eyebrow">// TRANSPARÊNCIA</span><p>Este projeto adapta workflows ao formato de plugin do Codex. A fonte de referência é open source sob MIT; o conteúdo e a implementação deste repositório são voltados ao Codex. Ferramentas externas não são simuladas: quando não há conexão, credencial ou dado, a skill informa a limitação.</p><div class="about-links"><a href="/codex-seo/CAPABILITY-MAP.md">MAPA DE CAPACIDADES ↗</a><a href="/codex-seo/EXTENSIONS.md">EXTENSÕES OPCIONAIS ↗</a><a href="https://github.com/AgriciDaniel/claude-seo">PROJETO DE REFERÊNCIA ↗</a></div></section></main><footer><span>CODEX SEO · OPEN SOURCE · MIT LICENSE</span><div><a href="https://github.com/CaduR/codex-seo">GITHUB ↗</a><a href="https://claude-seo.md/skills">REFERÊNCIA ↗</a></div></footer><script>const input=document.querySelector('#search'),cards=[...document.querySelectorAll('.skill-card')],empty=document.querySelector('#empty');input.addEventListener('input',()=>{{let n=0;for(const card of cards){{const show=card.dataset.search.includes(input.value.trim().toLocaleLowerCase('pt-BR'));card.hidden=!show;if(show)n++}}empty.hidden=n>0}});document.querySelector('.copy').addEventListener('click',async e=>{{await navigator.clipboard.writeText('codex plugin marketplace add CaduR/codex-seo');e.currentTarget.textContent='COPIADO'}});</script>'''
    (DOCS / "assets").mkdir(parents=True, exist_ok=True)
    (DOCS / "index.html").write_text(page("Seu time de SEO no Codex", "26 workflows de SEO para Codex: técnico, conteúdo, dados estruturados, local, GEO e muito mais.", content, BASE + "/"), encoding="utf-8")


if __name__ == "__main__":
    build()
