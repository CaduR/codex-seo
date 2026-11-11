---
title: "Como usar workflows de SEO no Codex"
description: "Instale o plugin, confirme o runtime local e escolha uma skill pelo trabalho que precisa resolver."
category: "Comece aqui"
date: "2026-11-10"
---

# Como usar workflows de SEO no Codex

O Codex SEO leva um catálogo de workflows para dentro do Codex. Cada skill orienta uma tarefa — de uma análise técnica a um briefing de conteúdo — e o servidor MCP local expõe apenas as ferramentas que o plugin oferece. A sessão ainda pode usar outras ferramentas que você tenha conectado.

## Instale e confira o runtime

Adicione `CaduR/codex-seo` como marketplace, instale o plugin na área de Plugins e inicie uma nova conversa. Peça ao Codex para executar `seo_doctor`; ele verifica se o runtime está pronto. Se faltar o ambiente Python, `seo_setup` cria um virtualenv na pasta de dados do usuário. Chromium é opcional e só é necessário para tarefas de navegador.

## Escolha a skill pelo objetivo

Use `$seo-audit` para pedir uma visão ampla ou uma skill focada como `$seo-technical`, `$seo-schema` ou `$seo-content`. Informe a URL, o contexto e a decisão que quer tomar. Se você já tem dados de Search Console ou um relatório, pode fornecê-los; o Codex deve separar o que observou do que não teve acesso.

## Entenda o limite entre instrução e ferramenta

As skills são instruções de workflow. As ferramentas locais estão disponíveis pelo MCP e cobrem um subconjunto de análises. O plugin não instala 19 subagentes independentes, não conecta suas contas do Google e não fornece bases comerciais de backlinks ou posições.

Antes de aceitar qualquer recomendação, confira a evidência, a data e a fonte. Um score heurístico pode ajudar a ordenar tarefas, mas não é uma métrica do Google nem uma previsão de tráfego.

## Próximos passos

- [Veja as 26 skills](/codex-seo/skills/)
- [Siga o guia de instalação](/codex-seo/install/)
- [Leia o mapa de capacidades](/codex-seo/CAPABILITY-MAP.md)
