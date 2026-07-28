# ADR-0002 — Organização por Diretorias

- **Status:** Aceito
- **Data:** 2026-07-27

## Contexto

O Projeto Jason adota uma Arquitetura Empresarial para organizar, de forma integrada, pessoas, agentes de IA, processos, dados, conhecimento e capacidades tecnológicas.

O ADR-0001 estabelece o modelo organizacional composto por CEO Jason, diretorias, departamentos, processos e agentes especializados. O ADR-0003 estabelece os departamentos como unidades operacionais vinculadas a diretorias. A arquitetura, portanto, requer uma camada organizacional intermediária que conecte a coordenação executiva à execução especializada.

O CEO Jason atua como orquestrador central do ecossistema: preserva o alinhamento institucional, prioriza demandas, coordena interdependências e consolida decisões. Esse papel não deve concentrar responsabilidades funcionais especializadas nem substituir a autonomia necessária aos domínios corporativos.

A organização por diretorias estabelece fronteiras funcionais claras, permite especialização por domínio e viabiliza o crescimento controlado do ecossistema sem comprometer a coerência arquitetural.

## Problema

Uma estrutura composta apenas por um orquestrador central, agentes individuais e departamentos operacionais não oferece uma camada suficiente para coordenar responsabilidades estratégicas e funcionais de maior amplitude.

Sem diretorias como unidades de responsabilidade, o Projeto Jason fica exposto a:

- sobreposição de responsabilidades entre agentes, departamentos e áreas funcionais;
- concentração excessiva de decisões no CEO Jason;
- dificuldade para definir accountability por domínio;
- acoplamento indevido entre capacidades especializadas;
- crescimento desorganizado de agentes, processos e integrações;
- perda de rastreabilidade sobre a origem, a autoridade e o impacto das decisões;
- dificuldade para coordenar decisões que envolvam mais de um domínio organizacional.

## Decisão

O Projeto Jason é organizado por diretorias como camada de responsabilidade funcional e estratégica entre o CEO Jason e os departamentos.

Cada diretoria representa um domínio de responsabilidade organizacional. Ela orienta e coordena os departamentos, processos e agentes associados ao seu domínio, em conformidade com as políticas corporativas, os limites de autonomia e a coordenação exercida pelo CEO Jason.

Essa organização preserva a execução distribuída: departamentos e agentes permanecem responsáveis por atividades especializadas, enquanto o CEO Jason mantém a integração, a priorização e a coerência global da arquitetura.

A composição de cada diretoria, seus departamentos, agentes, processos, indicadores e mecanismos operacionais é definida nos documentos organizacionais e operacionais específicos. Este ADR formaliza exclusivamente a adoção da organização por diretorias como padrão arquitetural.

## Princípios

- **Diretorias como domínios organizacionais:** diretorias representam domínios de responsabilidade organizacional, e não cargos ou indivíduos.
- **Clareza de responsabilidade:** cada diretoria possui um domínio funcional explícito, com responsabilidades que não se sobreponham indevidamente às de outras diretorias.
- **Autonomia governada:** diretorias podem tomar decisões dentro de seu domínio, desde que respeitem políticas corporativas, controles de risco, segurança, dados e limites de autoridade.
- **Coordenação central:** o CEO Jason coordena prioridades, interdependências e decisões institucionais, sem assumir a execução especializada dos domínios.
- **Execução distribuída:** departamentos e agentes executam atividades especializadas sob orientação funcional da diretoria correspondente.
- **Baixo acoplamento entre diretorias:** as diretorias devem interagir por interfaces, processos e decisões explicitamente definidos, evitando dependências implícitas ou responsabilidades compartilhadas sem governança.
- **Integração transversal:** iniciativas que afetem mais de uma diretoria utilizam mecanismos explícitos de comunicação, decisão, registro e acompanhamento.
- **Rastreabilidade:** responsabilidades, decisões e mudanças de escopo devem ser documentadas e auditáveis.
- **Evolução incremental:** a estrutura de diretorias evolui de forma controlada, preservando contratos organizacionais, processos e capacidades existentes.
- **Desacoplamento organizacional:** a evolução de uma diretoria não deve exigir mudanças não justificadas no núcleo de orquestração ou em domínios não relacionados.

## Consequências

A organização por diretorias cria uma estrutura de responsabilidade que permite ao Projeto Jason combinar especialização funcional, autonomia operacional e coordenação institucional.

Como consequências positivas, a arquitetura passa a ter fronteiras mais claras entre domínios, melhor distribuição de accountability, maior capacidade de expansão, integração mais estruturada entre áreas e melhores condições para governança, auditoria e evolução contínua.

Como consequências de atenção, cada diretoria precisa manter sua documentação sincronizada com a arquitetura oficial, explicitar suas interfaces com outros domínios e evitar a criação de silos. A inclusão ou alteração de uma diretoria exige análise de impacto e atualização dos documentos organizacionais relacionados.

## Referências

- ADR-0001 — Arquitetura Empresarial do Projeto Jason
- ADR-0003 — Organização por Departamentos
- ADR-0004 — Arquitetura de Agentes de IA
- ADR-0005 — Governança de Dados
- ARQUITETURA_EMPRESARIAL_V2.md
- ORGANOGRAMA.md
- Documentos da pasta `DIRETORIAS/`
- Documentos da pasta `DEPARTAMENTOS/`
- Documentos da pasta `AGENTES/`
- PROCESSO_DESENVOLVIMENTO_PRODUTO.md
- PROCESSO_GOVERNANCA_IA.md
