---
title: "Integrações SEO no Codex: o que é local e o que pode custar"
description: "Entenda a diferença entre as ferramentas locais do Codex SEO e conexões externas opcionais, como DataForSEO."
category: "Integrações"
date: "2026-11-10"
---

# Integrações SEO no Codex: o que é local e o que pode custar

O Codex SEO inclui um servidor MCP local para ferramentas de análise permitidas. Isso não significa que ele já esteja conectado ao Search Console, a uma base de backlinks ou a um provedor de SERP. Essas fontes exigem conexões independentes e permissões compatíveis.

## O que roda localmente

O runtime Python fica num ambiente isolado na pasta de dados do usuário. `seo_doctor` informa se ele está pronto, e `seo_setup` instala as dependências do plugin. `seo_analyze` executa scripts da lista permitida; as descrições das ferramentas mostram os limites da operação. O `seo_crawl` usa Unlighthouse, exige Node.js e limita o crawl a até 50 rotas.

## O que depende de conexão

Google Search Console, GA4, backlinks e dados atuais de SERP dependem de uma conexão autorizada ou de dados que você forneça. A integração oficial DataForSEO pode ser adicionada ao Codex por OAuth. Antes de uma chamada paga, descubra o endpoint e o preço atuais, apresente uma estimativa e espere aprovação.

Uma credencial configurada não prova que a conta tem acesso à propriedade ou cota disponível. E nenhum resultado externo deve ser tratado como garantido ou como instrução para alterar um site.

Veja o procedimento atual em [Extensões opcionais](/codex-seo/EXTENSIONS.md) e a [página da skill DataForSEO](/codex-seo/skills/seo-dataforseo/). Integrações pagas são opcionais; o catálogo de skills funciona sem elas, dentro dos dados e ferramentas disponíveis na sessão.
