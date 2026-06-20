import os
import json

# Define the base directory for agents
output_dir = r"C:\Users\engja\.gemini\antigravity\scratch\agentes-match\agentes"
os.makedirs(output_dir, exist_ok=True)

# Data for all 9 agents
agents_data = [
    {
        "filename": "orcamento-obras-sinapi-ia.html",
        "gem_number": "GEM 03",
        "name": "MatchOrça PRO",
        "keyword": "ia para orcamento de obras",
        "title": "MatchOrça PRO | IA para Orçamento de Obras e SINAPI",
        "meta_desc": "Crie orçamentos de obras, composições de custos unitários SINAPI/SICRO e cálculo de BDI automaticamente com o agente de Inteligência Artificial MatchOrça PRO.",
        "short_desc": "Orçamentos paramétricos, SINAPI/SICRO, cálculo de BDI, cronogramas físico-financeiros e análise de curva S em minutos.",
        "gemini_link": "https://gemini.google.com/gem/1jv5Hl2wbAo5W66J2NRH9uqP4MvXS4-ux?usp=sharing",
        "emoji": "💰",
        "color": "#D4AF37", # Gold
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="4" y="3" width="16" height="18" rx="2"/><line x1="8" y1="7" x2="16" y2="7"/><line x1="8" y1="11" x2="13" y2="11"/>
                <rect x="8" y="14" width="2" height="4"/><rect x="12" y="13" width="2" height="5"/><rect x="16" y="15" width="2" height="3"/>
            </svg>
        """,
        "features": [
            {"title": "Orçamentação Paramétrica & SINAPI", "desc": "Gera composições de custos detalhadas utilizando códigos SINAPI, SICRO ou TCPO para materiais, equipamentos e mão de obra."},
            {"title": "Cálculo de BDI Inteligente", "desc": "Estrutura o cálculo de BDI de forma justificada e compatível com as regras do TCU (IN TCU 05/2017) para obras públicas e privadas."},
            {"title": "Planejamento Físico-Financeiro", "desc": "Cria cronogramas de desembolso mensal e análises de Curva S para que você controle desvios de orçamento durante o projeto."},
            {"title": "Simulações de Viabilidade", "desc": "Analisa o impacto de oscilações de custos de insumos (CUB, INCC, commodities) e sugere alternativas de sistemas construtivos."}
        ],
        "prompts": [
            "Elabore uma planilha de quantitativos para uma casa térrea de 120m² com estrutura convencional, incluindo fundação, alvenaria, cobertura e acabamentos.",
            "Calcule o custo estimado de uma laje nervurada de 200m² utilizando a tabela SINAPI mais recente, detalhando materiais e mão de obra.",
            "Calcule o BDI adequado para uma obra pública de edificação no valor de R$ 5 milhões, seguindo a IN TCU 05/2017, detalhando cada componente.",
            "Monte um cronograma físico-financeiro para uma obra residencial de 18 meses, com distribuição mensal de custos por etapa construtiva."
        ],
        "faq": [
            {"q": "O MatchOrça PRO utiliza tabelas SINAPI atualizadas?", "a": "Sim. O agente é integrado à busca do Google e acessa dados atualizados do SINAPI por estado, gerando estimativas e composições em conformidade com o mercado atual."},
            {"q": "Consigo exportar o orçamento gerado para o Excel?", "a": "Com certeza. Ao gerar o orçamento no Google Gemini, você pode solicitar a formatação em tabela estruturada e copiá-la diretamente para o Excel ou Google Planilhas com um clique."},
            {"q": "O agente substitui o engenheiro orçamentista?", "a": "Não. O agente funciona como um copiloto técnico de alta velocidade, acelerando em até 90% a montagem e pesquisa inicial de composições, mas a validação e responsabilidade técnica final são do engenheiro."}
        ]
    },
    {
        "filename": "consultar-normas-nbr-abnt-ia.html",
        "gem_number": "GEM 05",
        "name": "NormaMatch PRO",
        "keyword": "ia normas abnt",
        "title": "NormaMatch PRO | IA para Consulta de Normas NBR e ABNT",
        "meta_desc": "Tire dúvidas sobre normas técnicas ABNT NBR (6118, 15575, 9050, etc.) em segundos com o consultor de Inteligência Artificial NormaMatch PRO.",
        "short_desc": "Sua enciclopédia interativa de NBRs. Esclarece exigências da NBR 15575 (Desempenho), NBR 6118 (Concreto) e muito mais.",
        "gemini_link": "https://gemini.google.com/gem/1dwzgUaDyQzmIHNQ5rIQhQPnHz2fuK980?usp=sharing",
        "emoji": "📋",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path d="M12 6c-1.5-1-4-1.5-6-1.5V18c2 0 4.5.5 6 1.5 1.5-1 4-1.5 6-1.5V4.5c-2 0-4.5.5-6 1.5z"/><line x1="12" y1="6" x2="12" y2="19.5"/>
            </svg>
        """,
        "features": [
            {"title": "Consulta Normativa Instantânea", "desc": "Responde dúvidas complexas de normas técnicas ABNT em segundos, indicando os itens específicos para dar embasamento técnico."},
            {"title": "Validação de Vigência", "desc": "Integrado à pesquisa em tempo real para verificar se uma NBR foi revogada, atualizada ou substituída pela ABNT."},
            {"title": "NBR 15575 de Desempenho", "desc": "Checklists e orientações rigorosas sobre vida útil de projeto (VUP), desempenho acústico, térmico e lumínico de edificações."},
            {"title": "Normas de Segurança (NRs)", "desc": "Consulte regras de segurança de canteiro de obras (NR-18, NR-35 e outras) para reduzir riscos jurídicos e operacionais."}
        ],
        "prompts": [
            "Analise se este projeto de edifício residencial de 8 pavimentos atende aos requisitos mínimos da NBR 15575 para desempenho acústico entre unidades.",
            "Verifique se as especificações de cobrimento de armadura do meu projeto estão adequadas para Classe de Agressividade Ambiental III conforme NBR 6118.",
            "Quais são os requisitos mínimos de desempenho térmico da NBR 15575 para paredes externas na Zona Bioclimática 8?",
            "Elabore um roteiro de inspeção para verificar conformidade com NBR 6118 em estruturas de concreto armado já executadas."
        ],
        "faq": [
            {"q": "O NormaMatch PRO tem acesso ao texto completo de todas as NBRs?", "a": "O agente possui uma ampla base de conhecimento sobre as principais NBRs da construção civil e está conectado ao Google Search para buscar dados atualizados, mas recomenda-se sempre confrontar dados críticos com as normas adquiridas formalmente na ABNT."},
            {"q": "Ele pode ajudar em processos de certificação PBQP-H?", "a": "Sim, fornecendo checklists de conformidade técnica, requisitos de controle de qualidade e validação de procedimentos em conformidade com as normas do SiAC/PBQP-H."},
            {"q": "O agente ajuda a elaborar justificativas para laudos técnicos?", "a": "Com certeza. Ele ajuda a redigir fundamentações técnicas impecáveis, citando os itens específicos e exigências das normas aplicáveis."}
        ]
    },
    {
        "filename": "analise-edital-licitacao-ia.html",
        "gem_number": "GEM 06",
        "name": "LegalMatch PRO",
        "keyword": "ia para licitacoes",
        "title": "LegalMatch PRO | IA para Licitações e Análise de Editais",
        "meta_desc": "Analise editais de obras, identifique riscos jurídicos, monte justificativas técnicas e minutas de recursos sob a Nova Lei de Licitações (Lei 14.133) com IA.",
        "short_desc": "Blindagem jurídica e inteligência administrativa para editais de obras públicas sob a Lei 14.133/2021 e orientações do TCU.",
        "gemini_link": "https://gemini.google.com/gem/17hhJkiI1p9uItxf5pOWpq3ltqDIN0K1U?usp=sharing",
        "emoji": "⚖️",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <line x1="12" y1="4" x2="12" y2="20"/><line x1="6" y1="20" x2="18" y2="20"/><line x1="5" y1="7" x2="19" y2="7"/>
                <path d="M5 7l-2.5 6a3 3 0 005 0z"/><path d="M19 7l-2.5 6a3 3 0 005 0z"/>
            </svg>
        """,
        "features": [
            {"title": "Análise de Riscos em Editais", "desc": "Faz uma varredura completa em editais de licitação, identificando exigências abusivas, restrições e riscos de engenharia."},
            {"title": "Minutas de Recursos e Impugnações", "desc": "Escreve minutas robustas para recursos administrativos ou impugnações fundamentadas de acordo com a Nova Lei de Licitações (Lei 14.133)."},
            {"title": "Equilíbrio Econômico-Financeiro", "desc": "Auxilia na fundamentação de pedidos de reequilíbrio, reajuste ou revisão contratual devido a oscilações de insumos ou imprevistos."},
            {"title": "Conformidade com Acórdãos do TCU", "desc": "Cruza exigências de editais com a jurisprudência mais atualizada do Tribunal de Contas da União para garantir conformidade."}
        ],
        "prompts": [
            "Analise este edital de licitação de pavimentação e aponte cláusulas restritivas ou abusivas na qualificação técnica que contradizem decisões do TCU.",
            "Elabore uma minuta de impugnação ao edital XYZ, alegando falta de parcelamento do objeto nos termos do Artigo 47 da Lei 14.133/2021.",
            "Desenvolva uma fundamentação técnica para pedido de reequilíbrio econômico devido ao aumento extraordinário de 35% no preço do asfalto.",
            "Quais são os requisitos mínimos para habilitação de atestado de responsabilidade técnica (CAT) para uma obra de ponte de concreto armado?"
        ],
        "faq": [
            {"q": "O LegalMatch PRO é atualizado com a Nova Lei de Licitações (Lei 14.133)?", "a": "Sim. O agente foi totalmente calibrado de acordo com a Lei 14.133/2021, jurisprudência do TCU e PNCP (Portal Nacional de Contratações Públicas)."},
            {"q": "Consigo analisar editais em formato PDF?", "a": "Sim. Você pode fazer upload do edital em PDF diretamente no Google Gemini (disponível na interface) e o agente fará a leitura e análise completa das seções indicadas."},
            {"q": "Ele serve também para elaboração de Termos de Referência?", "a": "Com certeza. O agente auxilia gestores públicos a estruturarem Termos de Referência (TR) e especificações técnicas de forma clara e blindada juridicamente."}
        ]
    },
    {
        "filename": "laudo-vistoria-cautelar-patologias-ia.html",
        "gem_number": "GEM 07",
        "name": "LaudoMatch PRO",
        "keyword": "ia laudo de vistoria cautelar",
        "title": "LaudoMatch PRO | IA para Laudo de Vistoria Cautelar e Patologias",
        "meta_desc": "Elabore laudos de vistoria cautelar de vizinhança, laudos de patologia predial e perícias técnicas em conformidade com as normas ABNT NBR utilizando IA.",
        "short_desc": "Estrutura e diagnósticos técnicos para engenharia diagnóstica, laudos de patologia predial, perícias judiciais e vistorias cautelares.",
        "gemini_link": "https://gemini.google.com/gem/1gZNu_M9sIGB59VHy_2XVWRAVxufO7kra?usp=sharing",
        "emoji": "🔍",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3a1 1 0 011-1h4a1 1 0 011 1v1"/><path d="M8.5 12.5l2 2 4-4"/>
            </svg>
        """,
        "features": [
            {"title": "Engenharia Diagnóstica Estruturada", "desc": "Estrutura laudos técnicos, vistorias cautelares de vizinhança e inspeções de manutenção em conformidade com as normas vigentes."},
            {"title": "Inspeção Predial (NBR 16747:2020)", "desc": "Auxilia na classificação sistemática de anomalias (endógenas, exógenas) e falhas, organizando por grau de prioridade técnica."},
            {"title": "Perícias Judiciais (NBR 13752)", "desc": "Ajuda peritos e assistentes técnicos a formatarem petições, laudos periciais e a responderem a quesitos técnicos judiciais com rigor."},
            {"title": "Análise Visual de Patologias", "desc": "Envie fotos de fissuras, infiltrações ou corrosão e obtenha pré-diagnósticos técnicos detalhados e causas prováveis."}
        ],
        "prompts": [
            "Estruture um laudo de vistoria cautelar de vizinhança para um imóvel lindeiro a uma obra de edifício residencial com subsolo escavado.",
            "Analise as possíveis causas de fissuras em formato de mapa em uma laje de cobertura exposta, sugerindo procedimentos de recuperação.",
            "Redija a resposta técnica ao quesito do juiz que questiona se a umidade na parede divisória provém de falha de impermeabilização da viga baldrame.",
            "Elabore uma lista de verificação de anomalias para inspeção predial de condomínio residencial com mais de 20 anos de construção."
        ],
        "faq": [
            {"q": "O LaudoMatch PRO consegue analisar fotos de rachaduras ou infiltrações?", "a": "Sim. Graças à capacidade multimodal do Gemini, você pode carregar imagens de patologias da construção diretamente no chat. O agente avalia as características visuais e propõe causas e soluções."},
            {"q": "O laudo gerado segue as normas da ABNT?", "a": "Sim, a redação e estrutura são orientadas pelas principais normas vigentes de engenharia diagnóstica, como a NBR 13752 (Perícias de Engenharia na Construção Civil) e NBR 16747 (Inspeção Predial)."},
            {"q": "Ele auxilia na emissão da ART?", "a": "O agente orienta sobre a correta classificação de atividades e seleção de códigos TOS na emissão da Anotação de Responsabilidade Técnica (ART) do laudo junto ao CREA."}
        ]
    },
    {
        "filename": "diario-obra-rdo-checklist-ia.html",
        "gem_number": "GEM 04",
        "name": "MatchObra PRO",
        "keyword": "diario de obra automatizado ia",
        "title": "MatchObra PRO | IA para Diário de Obra e Checklist de Qualidade",
        "meta_desc": "Automatize o preenchimento de Diários de Obra (RDO), checklists de controle de qualidade (FVS) e monitoramento de canteiro com Inteligência Artificial.",
        "short_desc": "Supervisor técnico virtual: RDO automático, checklists de qualidade baseados na NBR 15575 e conformidade de segurança (NR-18).",
        "gemini_link": "https://gemini.google.com/gem/1mV7RNTqWI6eUaPf5ibK3OkXk6yw4qWc-?usp=sharing",
        "emoji": "🏢",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="4" y="10" width="8" height="11"/><rect x="6.3" y="13" width="1.6" height="1.6"/><rect x="8.9" y="13" width="1.6" height="1.6"/>
                <rect x="6.3" y="16.5" width="1.6" height="1.6"/><rect x="8.9" y="16.5" width="1.6" height="1.6"/>
                <path d="M15 21V6h1l4 1"/><line x1="15" y1="9" x2="20" y2="9"/><line x1="18" y1="9" x2="18" y2="11"/>
            </svg>
        """,
        "features": [
            {"title": "Diário de Obra Rápido (RDO)", "desc": "Gera relatórios diários de obra estruturados contendo clima, efetivo de pessoal, atividades executadas, ocorrências e recebimento de materiais."},
            {"title": "Fichas de Verificação de Serviço", "desc": "Checklists de qualidade (FVS) baseados nas normas brasileiras para controle tecnológico (NBR 12655 - Concreto, NBR 15575 - Desempenho)."},
            {"title": "Auditor de NR-18 e Canteiro", "desc": "Identifica riscos físicos ou procedimentais em fotos e relata não conformidades com base nas normas regulamentadoras de segurança."},
            {"title": "Planejamento e Acompanhamento", "desc": "Organiza listas de tarefas semanais e identifica gargalos e caminho crítico na execução física para evitar atrasos."}
        ],
        "prompts": [
            "Estruture um RDO para o dia de hoje: Clima chuvoso pela manhã e limpo à tarde. Mão de obra: 5 carpinteiros, 8 armadores, 12 serventes. Atividade: Concretagem de 4 pilares do 2º pavimento.",
            "Crie uma FVS (Ficha de Verificação de Serviço) detalhada para a etapa de regularização de contrapiso interno em conformidade com as normas.",
            "Quais são os requisitos obrigatórios da NR-18 para montagem e uso seguro de andaimes suspensos (balancins) no canteiro?",
            "Elabore um texto de Diálogo Diário de Segurança (DDS) focado na importância do uso correto do cinto de segurança do tipo paraquedista em altura."
        ],
        "faq": [
            {"q": "Como o MatchObra PRO agiliza o preenchimento do RDO?", "a": "Você pode enviar anotações rápidas por texto, ou mesmo transcrição de áudios feitos no canteiro pelo celular, e o agente organiza tudo em um documento técnico e limpo pronto para arquivar."},
            {"q": "Ele ajuda no controle tecnológico do concreto?", "a": "Sim, auxiliando na conferência de dados de ensaios de corpos de prova (fck), prazos de desforma e cuidados durante o processo de cura úmida conforme a NBR 14931."},
            {"q": "O agente funciona offline?", "a": "O agente roda através do Google Gemini e requer acesso à internet. No entanto, você pode estruturar modelos de planilhas e checklists pelo agente para usar offline em campo no celular."}
        ]
    },
    {
        "filename": "calculo-estrutural-dimensionamento-ia.html",
        "gem_number": "GEM 08",
        "name": "EstruturaMatch PRO",
        "keyword": "ia calculo estrutural",
        "title": "EstruturaMatch PRO | IA para Dimensionamento e Cálculo Estrutural",
        "meta_desc": "Realize pré-dimensionamentos estruturais de concreto armado, vigas, pilares e sapatas em conformidade com as normas ABNT NBR utilizando IA.",
        "short_desc": "Dimensionamento e pré-dimensionamento de elementos estruturais (concreto, aço, madeira), reforços de patologias e análise da NBR 6118.",
        "gemini_link": "https://gemini.google.com/gem/10xfRN9InbZqg2rB4qZ09bd5o_5urYRST?usp=sharing",
        "emoji": "🏗️",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/>
                <line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/>
            </svg>
        """,
        "features": [
            {"title": "Pré-Dimensionamento Rápido", "desc": "Calcula de forma rápida seções estimadas para vigas, pilares, lajes e sapatas em função das cargas e vãos de projeto."},
            {"title": "NBR 6118 de Concreto Armado", "desc": "Verificação de conformidade de cobrimentos, domínios de deformação, taxa mínima de armaduras e cálculo de flexão simples."},
            {"title": "Análise de Patologias Estruturais", "desc": "Auxilia na identificação de causas de fissuras, deformações excessivas ou corrosão de armaduras em elementos estruturais existentes."},
            {"title": "Comparação de Sistemas", "desc": "Avalia o impacto financeiro e arquitetônico comparando concreto armado convencional, alvenaria estrutural e concreto protendido."}
        ],
        "prompts": [
            "Calcule a carga por metro linear para uma viga de baldrame com 6 metros de vão, considerando alvenaria de vedação de 19cm de espessura.",
            "Qual a armadura mínima necessária para uma laje maciça de 12cm de espessura com vão de 4x5 metros?",
            "Faça o pré-dimensionamento de pilares para um edifício de 10 pavimentos com área de influência de 25m² por pilar.",
            "Qual a flecha máxima admissível para uma laje de 6 metros de vão segundo os limites da NBR 6118?"
        ],
        "faq": [
            {"q": "O EstruturaMatch PRO calcula estruturas inteiras de prédios?", "a": "Não. O agente serve para pré-dimensionamento de elementos isolados, auditoria de cálculos e auxílio de tomada de decisão técnica. Projetos estruturais completos devem ser modelados em softwares dedicados (TQS, Eberick) e detalhados por engenheiro especialista."},
            {"q": "Ele faz cálculo de estruturas de aço e madeira?", "a": "Sim, fornece diretrizes de dimensionamento seguindo a NBR 8800 (Aço) e NBR 7190 (Madeira)."},
            {"q": "Ele detalha o processo de cura do concreto?", "a": "Sim. O agente fornece todas as recomendações de desforma e cura úmida normatizadas pela NBR 14931."}
        ]
    },
    {
        "filename": "avaliacao-imoveis-imobiliaria-ia.html",
        "gem_number": "GEM 09",
        "name": "AvaliaMatch PRO",
        "keyword": "ia avaliacao de imoveis",
        "title": "AvaliaMatch PRO | IA para Avaliação de Imóveis (NBR 14653)",
        "meta_desc": "Elabore laudos de avaliação de imóveis urbanos pelo Método Comparativo Direto de Dados de Mercado em conformidade com a NBR 14653 com IA.",
        "short_desc": "Engenharia de avaliações: método comparativo direto, tratamento estatístico de dados de mercado, laudos bancários e perícias.",
        "gemini_link": "https://gemini.google.com/gem/1V6d6n_LtnrlgD847HtWmjmC-baKKIc3V?usp=sharing",
        "emoji": "🏠",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
            </svg>
        """,
        "features": [
            {"title": "Método Comparativo de Mercado", "desc": "Estrutura avaliações com base na coleta de dados, fatores de homogeneização e regressões lineares conforme NBR 14653."},
            {"title": "Laudos de Garantia Bancária", "desc": "Agiliza a elaboração de laudos técnicos exigidos por bancos para financiamentos habitacionais e garantias reais."},
            {"title": "Métodos de Renda e Evolutivo", "desc": "Avaliação de aluguéis e taxas de capitalização (Método da Renda) ou cálculo de custo de reprodução de imóveis únicos (Método Evolutivo)."},
            {"title": "Tratamento Estatístico e Outliers", "desc": "Orienta no descarte de dados discrepantes da amostra utilizando o critério estatístico de Chauvenet."}
        ],
        "prompts": [
            "Estruture um laudo de avaliação de apartamento de 3 dormitórios seguindo o Método Comparativo Direto de Dados de Mercado da NBR 14653.",
            "Explique as regras da NBR 14653 para enquadramento do Grau de Fundamentação de uma avaliação imobiliária.",
            "Calcule a depreciação física de uma edificação comercial de 15 anos pelo método de Ross-Heidecke, sabendo que a vida útil de projeto é 50 anos.",
            "Como estruturar a justificativa técnica de um laudo de avaliação quando a amostra de mercado é reduzida na região?"
        ],
        "faq": [
            {"q": "O AvaliaMatch PRO realiza cálculos de regressão linear sozinho?", "a": "O agente orienta sobre a montagem da planilha, tratamento dos dados, cálculo dos fatores (fator de área, localização) e interpretação estatística. Para rodar a estatística inferencial complexa, recomenda-se usar softwares de apoio (como SISDEA ou TS-Sisvel) sob a orientação técnica estruturada pelo agente."},
            {"q": "Ele é válido para avaliações periciais judiciais?", "a": "Sim. A metodologia empregada nas respostas do agente baseia-se estritamente na NBR 14653 (partes 1 e 2), fornecendo embasamento técnico que resiste a impugnações judiciais."},
            {"q": "O agente ajuda a identificar o Grau de Precisão do laudo?", "a": "Sim, auxiliando na conferência dos critérios normativos exigidos para enquadramento de Grau I, II ou III de Fundamentação e Precisão."}
        ]
    },
    {
        "filename": "mockups-arquitetura-renders-ia.html",
        "gem_number": "GEM 10",
        "name": "ArquiMatch PRO",
        "keyword": "ia maquete 3d arquitetura",
        "title": "ArquiMatch PRO | IA para Renders e Design de Interiores",
        "meta_desc": "Gere prompts fotorrealistas para maquetes 3D, renders de fachada e designs de interiores utilizando IA. Otimizado para Imagen 3 e Veo 3.1.",
        "short_desc": "Consultoria em visualização arquitetônica, prompts fotorrealistas de render, memoriais conceituais e tours virtuais imersivos.",
        "gemini_link": "https://gemini.google.com/gem/1V5h5K0Q4voH1Pi0H-7WsfOI28fIMvBfC?usp=sharing",
        "emoji": "🎨",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.53 16.122l.188-.465a.6.6 0 00-.07-.528l-.307-.356a.6.6 0 00-.77 0l-.307.356a.6.6 0 00-.071.528l.189.465m6.858 0l.189-.465a.6.6 0 00-.07-.528l-.307-.356a.6.6 0 00-.77 0l-.307.356a.6.6 0 00-.07.528l.189.465m0 0a8.25 8.25 0 11-10.744 0m10.744 0a8.25 8.25 0 10-10.744 0M12 3v13.5"/>
            </svg>
        """,
        "features": [
            {"title": "Prompts Fotorrealistas de Render", "desc": "Cria comandos super-detalhados de fotografia arquitetônica (regras de lente, iluminação global, materiais PBR) para ferramentas de geração de imagem como Imagen 3."},
            {"title": "Memoriais Conceituais de Elite", "desc": "Redige memoriais descritivos conceituais e narrativas de projeto que encantam clientes e defendem as escolhas de design."},
            {"title": "Estudos de Insolação e Fachadas", "desc": "Gera prompts para simular a luz do sol nas fachadas em diferentes horários do dia, facilitando escolhas de brises e aberturas."},
            {"title": "Roteiros para Vídeos (Veo 3.1)", "desc": "Roteiriza tours 360° e sequências construtivas animadas de curta duração para apresentar o espaço de forma dinâmica."}
        ],
        "prompts": [
            "Elabore um prompt para o Imagen 3 gerar uma fachada moderna de edifício residencial de 12 pavimentos com elementos de concreto aparente e brises de madeira à luz do entardecer.",
            "Crie um roteiro detalhado para vídeo de tour virtual 360° de um apartamento de 80m² com estilo de design industrial contemporâneo.",
            "Redija o memorial descritivo para um projeto de casa de campo sustentável de 250m², com foco no uso de materiais locais e ventilação cruzada.",
            "Como otimizar a iluminação natural de um escritório corporativo voltado para a fachada oeste, de acordo com conceitos bioclimáticos?"
        ],
        "faq": [
            {"q": "O ArquiMatch PRO gera modelos 3D editáveis (BIM/CAD)?", "a": "Não. O agente cria mockups conceituais de imagem/vídeo e orientações de visualização e design, servindo para aprovação de conceito rápido. A modelagem 3D técnica continua exigindo softwares como Revit, SketchUp ou Archicad."},
            {"q": "Como funciona a geração de vídeo com o Veo 3.1?", "a": "O agente ajuda a estruturar a narrativa técnica e a descrever a trajetória da câmera, os elementos em movimento e a luz para que você use na ferramenta de geração de vídeos (Veo) do ecossistema Google."},
            {"q": "Posso usar os memoriais gerados para fins comerciais?", "a": "Sim, os memoriais descritivos e textos conceituais são de sua propriedade intelectual e podem ser usados comercialmente para apresentação de projetos a clientes."}
        ]
    },
    {
        "filename": "marketing-conseguir-clientes-ia.html",
        "gem_number": "GEM 02",
        "name": "PubliMatch PRO",
        "keyword": "marketing para engenheiros ia",
        "title": "PubliMatch PRO | IA para Marketing e Clientes na Engenharia",
        "meta_desc": "Descubra estratégias de marketing digital para engenheiros, copywriting para postagens de obras no Instagram e prospecção de clientes com IA.",
        "short_desc": "Marketing digital ético e estratégico (CREA/CONFEA), scripts de WhatsApp, SEO local e copy de alta conversão para engenheiros.",
        "gemini_link": "https://gemini.google.com/gem/1seZSo0D2p9CIE6T4S2QY__9xwVqhZnEE?usp=sharing",
        "emoji": "📢",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M10.34 15.84c-.68.34-1.34.08-1.34-.62V8.78c0-.7.66-.96 1.34-.62l5.22 2.61c.68.34.68.9 0 1.24l-5.22 2.61zM21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
        """,
        "features": [
            {"title": "Copywriting Técnico e Ético", "desc": "Cria roteiros, artigos e legendas altamente persuasivas respeitando as regras éticas de propaganda do CREA/CONFEA."},
            {"title": "Otimização de SEO Local", "desc": "Estratégias completas para posicionar seu escritório de engenharia no topo das buscas no Google Maps e Google Meu Negócio."},
            {"title": "Scripts de WhatsApp e Prospecção", "desc": "Scripts de cold approach e prospecção de clientes particulares e corporativos para venda de serviços técnicos de valor elevado."},
            {"title": "Planejamento Editorial Temático", "desc": "Cria cronogramas editoriais mensais baseados no seu nicho de atuação para atrair leads de forma qualificada."}
        ],
        "prompts": [
            "Crie um script de abordagem pelo WhatsApp para apresentar meus serviços de laudo de vistoria cautelar para síndicos de edifícios residenciais.",
            "Escreva um post para o LinkedIn focado em demonstrar a importância da engenharia diagnóstica antes da compra de um imóvel usado.",
            "Como otimizar meu perfil no Google Meu Negócio para ranquear em primeiro lugar na minha cidade para a busca 'calculista estrutural'?",
            "Roteirize um vídeo de 30 segundos para o Instagram demonstrando o andamento de uma concretagem de laje de forma dinâmica e didática."
        ],
        "faq": [
            {"q": "As estratégias geradas respeitam o código de ética do CREA?", "a": "Sim, todas as abordagens comerciais, copys e roteiros são planejados para valorizar o conhecimento do engenheiro sem infringir os limites de ética profissional definidos pelo CONFEA."},
            {"q": "O PubliMatch PRO cria imagens prontas para posts?", "a": "O agente auxilia na redação, nos roteiros e na descrição detalhada de imagens que você pode gerar utilizando o Imagen 3 ou criar em ferramentas como o Canva."},
            {"q": "Ele serve para quem atua em nichos muito específicos de engenharia?", "a": "Sim. Você pode definir seu nicho exato (saneamento, terraplenagem, pontes, patologia) e o agente calibrará a linguagem técnica para atrair o público ideal."}
        ]
    }
]

# Shared HTML Template
html_template = """<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">

<head>
  <meta charset="utf-8" />
  <meta content="width=device-width,initial-scale=1" name="viewport" />
  <title>{{title}}</title>
  <meta name="description" content="{{meta_desc}}" />

  <script src="https://cdn.tailwindcss.com"></script>
  <link
    href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap"
    rel="stylesheet" />

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            gold: '#D4AF37',
            goldLight: '#F4E4A0',
            goldDark: '#A68B2A',
            carbon: '#050505',
            carbonLight: '#111111',
            carbonMid: '#1a1a1a',
            carbonHover: '#222222',
          }},
          fontFamily: {{
            display: ['Playfair Display', 'serif'],
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }},
          animation: {{
            'blob': 'blob 7s infinite',
            'float': 'float 4s ease-in-out infinite',
          }},
          keyframes: {{
            blob: {{
              '0%': {{ transform: 'translate(0px, 0px) scale(1)' }},
              '33%': {{ transform: 'translate(30px, -50px) scale(1.1)' }},
              '66%': {{ transform: 'translate(-20px, 20px) scale(0.9)' }},
              '100%': {{ transform: 'translate(0px, 0px) scale(1)' }},
            }},
            float: {{
              '0%, 100%': {{ transform: 'translateY(0)' }},
              '50%': {{ transform: 'translateY(-10px)' }},
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      background-color: #050505;
      color: #e5e5e5;
      overflow-x: hidden;
    }}

    ::selection {{
      background: #D4AF37;
      color: #050505;
    }}

    .glass-card {{
      background: rgba(26, 26, 26, 0.4);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(212, 175, 55, 0.15);
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
      transition: all 0.4s ease;
    }}

    .glass-card:hover {{
      border-color: rgba(212, 175, 55, 0.4);
      background: rgba(30, 30, 30, 0.6);
      transform: translateY(-4px);
      box-shadow: 0 12px 40px 0 rgba(212, 175, 55, 0.1);
    }}

    .form-input {{
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #fff;
      transition: all 0.3s ease;
    }}

    .form-input:focus {{
      outline: none;
      border-color: #D4AF37;
      box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
      background: rgba(0, 0, 0, 0.8);
    }}

    .btn-premium {{
      background: linear-gradient(135deg, #A68B2A 0%, #D4AF37 50%, #F4E4A0 100%);
      background-size: 200% auto;
      color: #050505;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
      transition: all 0.4s ease;
      position: relative;
      overflow: hidden;
      z-index: 1;
    }}

    .btn-premium:hover {{
      background-position: right center;
      box-shadow: 0 6px 25px rgba(212, 175, 55, 0.5);
      transform: translateY(-2px);
    }}

    .btn-premium:active {{
      transform: translateY(1px);
    }}

    .btn-outline {{
      background: transparent;
      border: 1px solid rgba(212, 175, 55, 0.4);
      color: #D4AF37;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      transition: all 0.3s ease;
    }}

    .btn-outline:hover {{
      background: rgba(212, 175, 55, 0.1);
      border-color: #D4AF37;
    }}

    .text-gradient-gold {{
      background: linear-gradient(135deg, #e8c872 0%, #D4AF37 50%, #b38b1d 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}

    .gold-grid-bg {{
      background-image:
        linear-gradient(to right, rgba(212, 175, 55, 0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(212, 175, 55, 0.05) 1px, transparent 1px);
      background-size: 40px 40px;
    }}

    ::-webkit-scrollbar {{ width: 8px; }}
    ::-webkit-scrollbar-track {{ background: #050505; }}
    ::-webkit-scrollbar-thumb {{ background: #2A2A2A; border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #D4AF37; }}

    details > summary {{ list-style: none; cursor: pointer; }}
    details > summary::-webkit-details-marker {{ display: none; }}
    details[open] .faq-icon {{ transform: rotate(45deg); }}

    .reveal {{
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .reveal.active {{ opacity: 1; transform: translateY(0); }}

    .copy-btn {{
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .copy-btn:hover {{
      background: rgba(212, 175, 55, 0.15);
      border-color: #D4AF37;
    }}
  </style>

  <!-- Structured Data (JSON-LD) SoftwareApplication -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{name}",
    "operatingSystem": "All",
    "applicationCategory": "BusinessApplication",
    "description": "{{meta_desc}}",
    "offers": {{
      "@type": "Offer",
      "price": "47.00",
      "priceCurrency": "BRL"
    }}
  }}
  </script>

  <!-- Structured Data (JSON-LD) FAQ -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "{faq1_q}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{faq1_a}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{faq2_q}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{faq2_a}"
        }}
      }},
      {{
        "@type": "Question",
        "name": "{faq3_q}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{faq3_a}"
        }}
      }}
    ]
  }}
  </script>
</head>

<body class="antialiased font-sans">

  <!-- BACKGROUND GLOWS -->
  <div class="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
    <div class="absolute top-[-10%] left-[-10%] w-96 h-96 bg-gold/10 rounded-full mix-blend-screen filter blur-[100px] animate-blob"></div>
    <div class="absolute top-[20%] right-[-5%] w-[30rem] h-[30rem] bg-gold/5 rounded-full mix-blend-screen filter blur-[120px] animate-blob"></div>
    <div class="absolute bottom-[-20%] left-[20%] w-[40rem] h-[40rem] bg-white/5 rounded-full mix-blend-screen filter blur-[150px] animate-blob"></div>
  </div>

  <!-- HEADER -->
  <header class="fixed top-0 w-full z-50 bg-carbon/80 backdrop-blur-lg border-b border-white/5 transition-all duration-300" id="header">
    <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <a href="../index.html" class="font-display font-bold text-2xl tracking-tight text-white hover:opacity-85 transition-opacity">Agentes<span class="text-gold">Match</span></a>
        <div class="hidden md:flex items-center gap-2 border-l border-white/10 pl-3 ml-2">
          <span class="text-xs font-mono text-gray-500 uppercase tracking-widest">by</span>
          <a href="https://obramatch.com.br" target="_blank" rel="noopener" class="text-xs font-mono text-gold/70 hover:text-gold transition-colors">obramatch.com.br</a>
        </div>
      </div>
      <nav class="hidden lg:flex items-center gap-10 text-sm font-medium">
        <a href="#recursos" class="text-gray-400 hover:text-white transition-colors">Como funciona</a>
        <a href="#prompts" class="text-gray-400 hover:text-white transition-colors">Prompts prontos</a>
        <a href="#faq" class="text-gray-400 hover:text-white transition-colors">Dúvidas</a>
      </nav>
      <div class="flex items-center gap-4">
        <a href="../index.html" class="btn-outline px-5 py-2 rounded text-xs">Voltar para Home</a>
      </div>
    </div>
  </header>

  <main class="pt-20">

    <!-- HERO -->
    <section class="relative min-h-[85vh] flex items-center gold-grid-bg" id="inicio">
      <div class="max-w-7xl mx-auto px-6 py-12 lg:py-24 grid lg:grid-cols-12 gap-12 lg:gap-10 items-center">

        <!-- Left: Copy & Form -->
        <div class="lg:col-span-7 reveal">
          <div class="inline-flex items-center gap-3 bg-white/5 border border-white/10 rounded-full px-4 py-1.5 mb-8 backdrop-blur-sm">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-gold opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-gold"></span>
            </span>
            <span class="font-mono text-[11px] text-white font-bold uppercase tracking-widest">{gem_number} · Especialista Oficial</span>
          </div>

          <h1 class="font-display text-4xl sm:text-5xl lg:text-6xl font-bold leading-[1.08] tracking-tight mb-6 text-white">
            Domine as buscas de<br />
            {keyword} com <span class="text-gradient-gold">{name}</span>
          </h1>

          <p class="text-lg lg:text-xl text-gray-400 mb-8 max-w-2xl leading-relaxed font-light">
            {short_desc} Tenha um copiloto de inteligência artificial de alta performance integrado ao seu Google Gemini.
          </p>

          <!-- Form inline or box -->
          <div class="glass-card rounded-2xl p-6 lg:p-8 border border-white/10 relative max-w-xl">
            <div id="leadFormContainer">
              <h3 class="text-lg font-bold text-white mb-2">Libere o acesso ao {name} no Gemini</h3>
              <p class="text-xs text-gray-400 mb-6">Preencha os dados e abra o agente gratuitamente de imediato.</p>
              
              <form id="agentForm" class="space-y-4">
                <div class="grid sm:grid-cols-2 gap-4">
                  <div>
                    <label for="name" class="block text-[10px] font-medium text-gray-400 mb-1 ml-1 uppercase">Nome completo</label>
                    <input type="text" id="name" required class="form-input w-full px-4 py-3 rounded-lg text-xs" placeholder="Ex: João Silva">
                  </div>
                  <div>
                    <label for="email" class="block text-[10px] font-medium text-gray-400 mb-1 ml-1 uppercase">E-mail</label>
                    <input type="email" id="email" required class="form-input w-full px-4 py-3 rounded-lg text-xs" placeholder="seu@email.com">
                  </div>
                </div>
                <div>
                  <label for="whatsapp" class="block text-[10px] font-medium text-gray-400 mb-1 ml-1 uppercase">WhatsApp (com DDD)</label>
                  <input type="tel" id="whatsapp" required class="form-input w-full px-4 py-3 rounded-lg text-xs" placeholder="(81) 99999-9999">
                </div>

                <button type="submit" class="btn-premium w-full py-3.5 rounded-lg mt-4 text-xs font-bold uppercase tracking-wider flex justify-center items-center">
                  <span>Abrir Agente no Gemini ↗</span>
                </button>
              </form>
            </div>

            <div id="successContainer" class="hidden text-center py-6">
              <div class="w-12 h-12 bg-green-500/20 rounded-full flex items-center justify-center mx-auto mb-4 border border-green-500/50">
                <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
              </div>
              <h3 class="text-lg font-bold text-white mb-2">Acesso Concedido!</h3>
              <p class="text-xs text-gray-400 mb-6">Abrimos o agente {name} no seu Gemini em uma nova janela.</p>
              <a href="{gemini_link}" target="_blank" rel="noopener" class="btn-premium px-8 py-3 rounded text-xs inline-block">Abrir no Gemini</a>
            </div>
          </div>
        </div>

        <!-- Right: Interactive SVG Interface Mock -->
        <div class="lg:col-span-5 reveal relative">
          <div class="absolute -inset-1 bg-gradient-to-r from-gold/20 to-transparent rounded-2xl blur-lg opacity-40"></div>
          <div class="glass-card rounded-2xl p-6 relative z-10 border border-white/10">
            <div class="flex items-center justify-between pb-4 border-b border-white/5 mb-4">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-red-500/80"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-yellow-500/80"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-green-500/80"></span>
              </div>
              <span class="font-mono text-[10px] text-gray-500 tracking-wider">Google Gemini API / {name}</span>
            </div>
            
            <!-- Mock Chat Area -->
            <div class="space-y-4 min-h-[300px] flex flex-col justify-end text-xs">
              <div class="flex justify-end">
                <div class="bg-white/5 border border-white/10 rounded-2xl rounded-tr-sm px-4 py-3 max-w-[85%] text-gray-300">
                  Como o <b class="text-white font-medium">{name}</b> pode me ajudar na rotina diária como engenheiro civil?
                </div>
              </div>
              <div class="flex justify-start">
                <div class="bg-gold/10 border border-gold/20 rounded-2xl rounded-tl-sm px-4 py-3 max-w-[90%] text-gray-200">
                  <div class="flex items-center gap-2 mb-2 font-mono text-[10px] text-gold font-bold">
                    {icon_svg}
                    <span>{name}</span>
                  </div>
                  <p class="leading-relaxed">Como um super agente do Gemini, fui moldado especificamente para o pilar de <b>{keyword}</b>. Analiso regulamentações, formato memoriais e orçamentos, e elaboro diagnósticos de forma técnica e precisa em minutos.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- FEATURES -->
    <section class="py-24 bg-carbonLight/50 border-y border-white/5" id="recursos">
      <div class="max-w-6xl mx-auto px-6">
        <div class="text-center mb-16 reveal">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Recursos e Funcionalidades</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 mb-4 text-white">Como o {name} funciona na prática</h2>
          <p class="text-gray-400 max-w-2xl mx-auto">Desenvolvido por especialistas da construção, integrando conhecimentos reais a fluxos ágeis de IA.</p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 reveal">
          {features_cards}
        </div>
      </div>
    </section>

    <!-- PROMPTS SWIPE FILE -->
    <section class="py-24 relative" id="prompts">
      <div class="max-w-5xl mx-auto px-6 reveal">
        <div class="text-center mb-16">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Acervo de Prompts</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 mb-4 text-white">Copie e use no seu Gemini</h2>
          <p class="text-gray-400">Modelos de comando altamente precisos para extrair os melhores resultados técnicos.</p>
        </div>

        <div class="space-y-6">
          {prompts_cards}
        </div>
      </div>
    </section>

    <!-- MONETIZATION / CTA -->
    <section class="py-24 bg-carbonLight border-y border-white/5 relative">
      <div class="absolute inset-0 bg-gold/5 pointer-events-none"></div>
      <div class="max-w-4xl mx-auto px-6 text-center reveal relative z-10">
        <h2 class="font-display text-4xl lg:text-5xl font-bold text-white mb-6">Eleve o nível do seu escritório técnico</h2>
        <p class="text-gray-400 mb-8 max-w-2xl mx-auto">O {name} faz parte da suíte premium de 9 agentes do Agentes Match. Garanta o acesso a todos os agentes e economize mais de 50%!</p>
        
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <a href="{checkout_link}" target="_blank" rel="noopener" class="btn-premium px-8 py-4 rounded-lg text-sm text-center">Adquirir Pacote Completo (9 Agentes)</a>
          <a href="#inicio" class="btn-outline px-8 py-4 rounded-lg text-sm text-center">Testar Este Agente Grátis</a>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="py-24 relative" id="faq">
      <div class="max-w-4xl mx-auto px-6">
        <div class="text-center mb-16 reveal">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Perguntas Frequentes</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 mb-4 text-white">Dúvidas comuns sobre o {name}</h2>
        </div>

        <div class="space-y-4 reveal">
          {faq_elements}
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="bg-carbonLight border-t border-white/5 pt-16 pb-12">
    <div class="max-w-7xl mx-auto px-6">
      
      <!-- Cross linking section -->
      <div class="grid grid-cols-2 md:grid-cols-5 gap-8 pb-12 border-b border-white/5 text-xs text-gray-400">
        <div class="col-span-2">
          <div class="font-display font-bold text-lg text-white mb-4">Agentes<span class="text-gold">Match</span></div>
          <p class="max-w-xs leading-relaxed text-gray-500 font-light mb-4">Suíte de Inteligência Artificial nativa do Google Gemini moldada especificamente para o cotidiano de engenheiros civis.</p>
          <span class="text-[10px] text-gray-600 font-mono">Powered by <a href="https://obramatch.com.br" class="text-gold/70 hover:text-gold">obramatch.com.br</a></span>
        </div>
        <div>
          <h4 class="font-bold text-white uppercase tracking-wider mb-4 font-mono text-[10px]">Agentes Principais</h4>
          <ul class="space-y-3">
            <li><a href="orcamento-obras-sinapi-ia.html" class="hover:text-gold transition-colors">MatchOrça PRO (Orçamentos)</a></li>
            <li><a href="consultar-normas-nbr-abnt-ia.html" class="hover:text-gold transition-colors">NormaMatch PRO (Normas)</a></li>
            <li><a href="analise-edital-licitacao-ia.html" class="hover:text-gold transition-colors">LegalMatch PRO (Licitações)</a></li>
            <li><a href="laudo-vistoria-cautelar-patologias-ia.html" class="hover:text-gold transition-colors">LaudoMatch PRO (Laudos)</a></li>
          </ul>
        </div>
        <div>
          <h4 class="font-bold text-white uppercase tracking-wider mb-4 font-mono text-[10px]">Gestão e Produção</h4>
          <ul class="space-y-3">
            <li><a href="diario-obra-rdo-checklist-ia.html" class="hover:text-gold transition-colors">MatchObra PRO (Gestão)</a></li>
            <li><a href="calculo-estrutural-dimensionamento-ia.html" class="hover:text-gold transition-colors">EstruturaMatch (Cálculo)</a></li>
            <li><a href="avaliacao-imoveis-imobiliaria-ia.html" class="hover:text-gold transition-colors">AvaliaMatch (Avaliações)</a></li>
          </ul>
        </div>
        <div>
          <h4 class="font-bold text-white uppercase tracking-wider mb-4 font-mono text-[10px]">Marketing e Visual</h4>
          <ul class="space-y-3">
            <li><a href="mockups-arquitetura-renders-ia.html" class="hover:text-gold transition-colors">ArquiMatch PRO (Design)</a></li>
            <li><a href="marketing-conseguir-clientes-ia.html" class="hover:text-gold transition-colors">PubliMatch PRO (Clientes)</a></li>
            <li><a href="../index.html" class="hover:text-gold transition-colors">Voltar à Página Principal</a></li>
          </ul>
        </div>
      </div>

      <div class="flex flex-col md:flex-row justify-between items-center gap-6 pt-8 text-xs text-gray-500 font-mono">
        <p>© 2026 ObraMatch. Todos os direitos reservados. Projetos executados exigem a responsabilidade técnica de profissional habilitado.</p>
        <div class="flex gap-6">
          <a href="https://obramatch.com.br" target="_blank" rel="noopener" class="hover:text-white transition-colors">obramatch.com.br</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    // Reveal Animations
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }}
      }});
    }}, {{ threshold: 0.1, rootMargin: "0px 0px -50px 0px" }});

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Form logic simulating Lead integration and redirecting
    const form = document.getElementById('agentForm');
    const leadFormContainer = document.getElementById('leadFormContainer');
    const successContainer = document.getElementById('successContainer');

    form.addEventListener('submit', (e) => {{
      e.preventDefault();
      
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const whatsapp = document.getElementById('whatsapp').value;
      
      // Simulate API saving
      leadFormContainer.classList.add('hidden');
      successContainer.classList.remove('hidden');
      
      // Open Gemini link in a new window/tab
      window.open("{gemini_link}", "_blank");
    }});

    // Header Dynamic Blur
    window.addEventListener('scroll', () => {{
      const header = document.getElementById('header');
      if (window.scrollY > 20) {{
        header.classList.add('bg-carbon/90', 'shadow-lg');
        header.classList.remove('bg-carbon/80');
      }} else {{
        header.classList.add('bg-carbon/80');
        header.classList.remove('bg-carbon/90', 'shadow-lg');
      }}
    }});

    // Prompts Copy function
    function copyPrompt(btn, id) {{
      const textEl = document.getElementById(id);
      navigator.clipboard.writeText(textEl.innerText).then(() => {{
        const originalText = btn.innerText;
        btn.innerText = 'COPIADO!';
        btn.classList.add('text-green-400', 'border-green-400');
        setTimeout(() => {{
          btn.innerText = originalText;
          btn.classList.remove('text-green-400', 'border-green-400');
        }}, 2000);
      }});
    }}
  </script>
</body>

</html>
"""

# Helper function to generate features cards
def make_features_cards(features):
    cards_html = ""
    for f in features:
        cards_html += f"""
          <div class="glass-card rounded-2xl p-6 lg:p-8">
            <h3 class="font-display text-xl font-bold text-white mb-3">{{f['title']}}</h3>
            <p class="text-sm text-gray-400 leading-relaxed font-light">{{f['desc']}}</p>
          </div>
        """
    return cards_html

# Helper function to generate prompts cards
def make_prompts_cards(prompts, prefix_id):
    cards_html = ""
    for i, p in enumerate(prompts):
        id_str = f"prompt_{{prefix_id}}_{{i}}"
        cards_html += f"""
          <div class="glass-card rounded-2xl p-6 lg:p-8 border border-white/10 group">
            <div class="flex justify-between items-center mb-4 pb-4 border-b border-white/5">
              <div class="flex items-center gap-3">
                <span class="w-2 h-2 rounded-full bg-gold"></span>
                <span class="font-mono text-xs text-white uppercase tracking-widest font-bold">Prompt {{i+1}}</span>
              </div>
              <button onclick="copyPrompt(this, '{{id_str}}')" class="copy-btn text-[10px] font-mono text-gold border border-gold/30 px-3 py-1.5 rounded hover:bg-gold hover:text-carbon transition-colors">
                📋 Copiar Prompt
              </button>
            </div>
            <div class="font-mono text-sm text-gray-300 leading-relaxed font-light" id="{{id_str}}">{{p}}</div>
          </div>
        """
    return cards_html

# Helper function to generate FAQ elements
def make_faq_elements(faq):
    faq_html = ""
    for i, item in enumerate(faq):
        faq_html += f"""
          <details class="glass-card rounded-xl p-5 border border-white/10" {{"open" if i==0 else ""}}>
            <summary class="flex justify-between items-center font-display font-semibold text-white">
              <span>{{item['q']}}</span>
              <span class="faq-icon text-gold transition-transform duration-300 font-mono text-xl">+</span>
            </summary>
            <div class="mt-4 text-sm text-gray-400 leading-relaxed font-light border-t border-white/5 pt-4">
              {{item['a']}}
            </div>
          </details>
        """
    return faq_html

# Generate the pages
for agent in agents_data:
    features_cards = make_features_cards(agent["features"])
    prompts_cards = make_prompts_cards(agent["prompts"], agent["name"].lower().replace(" ", "").replace("ç", "c").replace("á", "a"))
    faq_elements = make_faq_elements(agent["faq"])
    
    # Format the final HTML using double braces for templates and formatting parameters
    file_content = html_template.replace("{{title}}", agent["title"])\
                                .replace("{{meta_desc}}", agent["meta_desc"])\
                                .format(
                                    name=agent["name"],
                                    gem_number=agent["gem_number"],
                                    keyword=agent["keyword"],
                                    short_desc=agent["short_desc"],
                                    gemini_link=agent["gemini_link"],
                                    icon_svg=agent["icon_svg"],
                                    features_cards=features_cards,
                                    prompts_cards=prompts_cards,
                                    faq_elements=faq_elements,
                                    checkout_link=agent["checkout_link"],
                                    faq1_q=agent["faq"][0]["q"],
                                    faq1_a=agent["faq"][0]["a"],
                                    faq2_q=agent["faq"][1]["q"],
                                    faq2_a=agent["faq"][1]["a"],
                                    faq3_q=agent["faq"][2]["q"],
                                    faq3_a=agent["faq"][2]["a"]
                                )
    
    # Write file
    file_path = os.path.join(output_dir, agent["filename"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)
        
    print(f"Generated: {agent['filename']}")
