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
        "category": "Orçamento e Custos",
        "keyword": "ia para orcamento de obras",
        "title": "MatchOrça PRO | IA para Orçamento de Obras e SINAPI",
        "meta_desc": "Crie orçamentos de obras, composições de custos unitários SINAPI/SICRO e cálculo de BDI automaticamente com o agente de Inteligência Artificial MatchOrça PRO.",
        "short_desc": "Orçamentos paramétricos, SINAPI/SICRO, cálculo de BDI, cronogramas físico-financeiros e análise de curva S em minutos.",
        "gemini_link": "https://gemini.google.com/gem/1jv5Hl2wbAo5W66J2NRH9uqP4MvXS4-ux?usp=sharing",
        "emoji": "💰",
        "color": "#D4AF37", # Gold
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Orçamentos de Obras 90% Mais Rápidos e 100% Alinhados ao SINAPI",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="4" y="3" width="16" height="18" rx="2"/><line x1="8" y1="7" x2="16" y2="7"/><line x1="8" y1="11" x2="13" y2="11"/>
                <rect x="8" y="14" width="2" height="4"/><rect x="12" y="13" width="2" height="5"/><rect x="16" y="15" width="2" height="3"/>
            </svg>
        """,
        "problem_now": "Elaborar orçamentos de obras e composições de custos unitários (CPU) manualmente é exaustivo. Você passa horas pesquisando códigos SINAPI/SICRO desatualizados, calculando BDI sem justificativa técnica robusta e montando cronogramas físico-financeiros complexos no Excel. Um único erro de quantitativo ou índice pode destruir a margem de lucro de um projeto inteiro.",
        "transformation": "Com o MatchOrça PRO, você transforma esse gargalo em uma vantagem competitiva. O agente analisa o escopo do seu projeto e sugere as composições de custos unitários exatas utilizando códigos SINAPI. Em poucos minutos, você gera cálculos de BDI estruturados, cronogramas físico-financeiros e análises de Curva S prontos para validação final e importação nas suas planilhas.",
        "features": [
            {"title": "Orçamentação Paramétrica & SINAPI", "desc": "Gera composições de custos detalhadas utilizando códigos SINAPI ou SICRO para materiais, equipamentos e mão de obra.", "benefit": "Precisão instantânea em CPUs de mercado."},
            {"title": "Cálculo de BDI Inteligente", "desc": "Estrutura o cálculo de BDI de forma justificada e compatível com as regras do TCU (IN TCU 05/2017) para obras públicas e privadas.", "benefit": "Segurança jurídica e técnica em licitações."},
            {"title": "Planejamento Físico-Financeiro", "desc": "Cria cronogramas de desembolso mensal e análises de Curva S para que você controle desvios de orçamento durante o projeto.", "benefit": "Visão gerencial clara do fluxo de caixa da obra."},
            {"title": "Simulações de Viabilidade", "desc": "Analisa o impacto de oscilações de custos de insumos (CUB, INCC, commodities) e sugere alternativas de sistemas construtivos.", "benefit": "Decisões de compra otimizadas e economia."}
        ],
        "steps": [
            {"step": "1", "title": "Definir o Escopo da Obra", "desc": "Insira o tipo de obra, área construtiva, padrão (alto, médio, baixo) e o estado de referência do SINAPI."},
            {"step": "2", "title": "Pesquisa e Cálculo de Custos", "desc": "O MatchOrça PRO consulta as bases de custos e calcula a viabilidade econômica, BDI e cronograma preliminar."},
            {"step": "3", "title": "Estruturação das Planilhas", "desc": "O agente fornece tabelas estruturadas de insumos, custos diretos, indiretos e curvas de desembolso."},
            {"step": "4", "title": "Validação e Exportação", "desc": "Você revisa o resultado técnico final, exporta os dados para o Excel ou software de engenharia e aplica na sua obra."}
        ],
        "prompts": [
            {
                "name": "Verificação Inicial de Custos",
                "objective": "Gerar uma estimativa de custo preliminar paramétrica para uma edificação.",
                "instruction": "Você é o MatchOrça PRO. Elabore uma estimativa de custo paramétrico para uma edificação residencial com [ÁREA] m² de área construída, padrão construtivo [PADRÃO] (alto, médio ou baixo), localizada em [ESTADO], utilizando como referência os valores de CUB mais recentes para este mês.",
                "placeholders": "[ÁREA] (ex: 150), [PADRÃO] (ex: Médio), [ESTADO] (ex: PE)"
            },
            {
                "name": "Composição de Custo Unitário (CPU)",
                "objective": "Montar a composição de custo detalhada de um serviço específico baseado no SINAPI.",
                "instruction": "Você é o MatchOrça PRO. Monte a composição de custo unitário detalhada para a execução de [SERVIÇO] utilizando os códigos e índices de produtividade padrão do SINAPI para o estado de [ESTADO]. Separe claramente em materiais (com consumo), mão de obra (com coeficientes de produtividade) e equipamentos.",
                "placeholders": "[SERVIÇO] (ex: Alvenaria de vedação de bloco cerâmico 14cm), [ESTADO] (ex: SP)"
            },
            {
                "name": "Cálculo de BDI",
                "objective": "Estruturar a taxa de BDI justificada para uma proposta comercial.",
                "instruction": "Você é o MatchOrça PRO. Estruture o memorial de cálculo justificado para a taxa de BDI (Benefícios e Despesas Indiretas) de uma obra [TIPO_OBRA] (privada ou pública) com valor estimado de [VALOR_ESTIMADO]. Siga as orientações e faixas recomendadas pelo TCU (Acórdão 2622/2013), detalhando administração central, seguros, riscos, despesas financeiras, tributos e margem de lucro líquida.",
                "placeholders": "[TIPO_OBRA] (ex: pública de edificações), [VALOR_ESTIMADO] (ex: R$ 3.000.000,00)"
            },
            {
                "name": "Cronograma Físico-Financeiro",
                "objective": "Gerar a distribuição mensal de desembolso econômico da obra.",
                "instruction": "Você é o MatchOrça PRO. Crie um cronograma físico-financeiro preliminar para uma obra residencial de [PRAZO_MESES] meses com orçamento total de [VALOR_TOTAL]. Distribua as etapas construtivas logicamente (serviços preliminares, infraestrutura, superestrutura, vedações, instalações, acabamentos) e apresente o percentual e valor de desembolso previsto para cada mês.",
                "placeholders": "[PRAZO_MESES] (ex: 12), [VALOR_TOTAL] (ex: R$ 850.000,00)"
            }
        ],
        "benefits": [
            "Economia de Tempo: Reduza em até 90% o tempo gasto procurando códigos e calculando índices de BDI.",
            "Segurança Técnica: Embasamento nos parâmetros do TCU e tabelas SINAPI atualizadas por estado.",
            "Organização Operacional: Cronogramas e CPU estruturados de forma padronizada prontos para exportação."
        ],
        "for_whom": [
            "Engenheiros Orçamentistas: que buscam velocidade na montagem de CPUs e estimativas de licitações.",
            "Construtoras e Incorporadoras: que precisam validar orçamentos e simular viabilidade rápida de obras.",
            "Profissionais Autônomos: que desejam apresentar propostas comerciais com BDI e cronogramas profissionais."
        ],
        "included": [
            "Acesso imediato ao agente MatchOrça PRO no Google Gemini.",
            "4 prompts estruturados de alta performance para orçamentação e planejamento.",
            "Guia rápido de uso integrado com links e documentação técnica.",
            "Atualizações automáticas do agente conforme evolução do ecossistema Gemini."
        ],
        "faq": [
            {"q": "O MatchOrça PRO utiliza tabelas SINAPI atualizadas?", "a": "Sim. O agente é integrado à busca do Google e acessa dados atualizados do SINAPI por estado, gerando estimativas e composições em conformidade com o mercado atual."},
            {"q": "Consigo exportar o orçamento gerado para o Excel?", "a": "Com certeza. Ao gerar o orçamento no Google Gemini, você pode solicitar a formatação em tabela estruturada e copiá-la diretamente para o Excel ou Google Planilhas com um clique."},
            {"q": "O agente substitui o engenheiro orçamentista?", "a": "Não. O agente funciona como um copiloto técnico de alta velocidade, acelerando em até 90% a montagem e pesquisa inicial de composições, mas a validação e responsabilidade técnica final são do engenheiro."},
            {"q": "Preciso ter conhecimento de IA para usar o MatchOrça PRO?", "a": "Nenhum. Basta copiar os prompts estruturados fornecidos na landing page, preencher as variáveis entre colchetes e colar no chat do Google Gemini."},
            {"q": "O acesso é vitalício?", "a": "Sim. Ao adquirir o pacote de agentes do Agentes Match, você tem acesso vitalício aos prompts e atualizações dos agentes oficiais."},
            {"q": "Quais são as limitações do agente?", "a": "O agente auxilia a pesquisar e estruturar dados com base em prompts avançados, mas não realiza integrações de banco de dados diretamente em softwares de ERP proprietários sem intervenção humana de cópia de tabelas."},
            {"q": "Qual o modelo de licença do agente?", "a": "O agente é disponibilizado através de um link compartilhado do Google Gemini, configurado como um especialista personalizado pronto para uso imediato no seu navegador."},
            {"q": "Existe garantia de reembolso?", "a": "Sim, oferecemos garantia incondicional de 7 dias. Se você testar e achar que a suíte não economiza seu tempo de engenharia, basta solicitar o reembolso integral."}
        ]
    },
    {
        "filename": "consultar-normas-nbr-abnt-ia.html",
        "gem_number": "GEM 05",
        "name": "NormaMatch PRO",
        "category": "Normas e Conformidade",
        "keyword": "ia normas abnt",
        "title": "NormaMatch PRO | IA para Consulta de Normas NBR e ABNT",
        "meta_desc": "Tire dúvidas sobre normas técnicas ABNT NBR (6118, 15575, 9050, etc.) em segundos com o consultor de Inteligência Artificial NormaMatch PRO.",
        "short_desc": "Sua enciclopédia interativa de NBRs. Esclarece exigências da NBR 15575 (Desempenho), NBR 6118 (Concreto) e muito mais.",
        "gemini_link": "https://gemini.google.com/gem/1dwzgUaDyQzmIHNQ5rIQhQPnHz2fuK980?usp=sharing",
        "emoji": "📋",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Tire Qualquer Dúvida sobre Normas ABNT NBR em Segundos",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path d="M12 6c-1.5-1-4-1.5-6-1.5V18c2 0 4.5.5 6 1.5 1.5-1 4-1.5 6-1.5V4.5c-2 0-4.5.5-6 1.5z"/><line x1="12" y1="6" x2="12" y2="19.5"/>
            </svg>
        """,
        "problem_now": "Pesquisar diretrizes de normas técnicas ABNT NBR consome um tempo precioso que deveria estar sendo usado no projeto. O catálogo é imenso, as normas são constantemente atualizadas ou canceladas, e ler centenas de páginas para encontrar um simples valor de cobrimento nominal ou nível de desempenho acústico é ineficiente e abre margem para erros graves que podem invalidar projetos inteiros na prefeitura.",
        "transformation": "Com o NormaMatch PRO, você tem um consultor normativo virtual de plantão. O agente sintetiza as exigências de normas cruciais como a NBR 15575 (Desempenho), NBR 6118 (Concreto Armado) e NBR 9050 (Acessibilidade) em segundos. Ele ajuda a estruturar listas de conformidade, verificar a vigência de exigências e embasar tecnicamente seus relatórios com as cláusulas corretas.",
        "features": [
            {"title": "Consulta Normativa Instantânea", "desc": "Responde dúvidas complexas de normas técnicas ABNT em segundos, indicando os itens específicos para dar embasamento técnico.", "benefit": "Embasamento técnico sem leitura manual exaustiva."},
            {"title": "Validação de Vigência", "desc": "Integrado à pesquisa em tempo real para verificar se uma NBR foi revogada, atualizada ou substituída pela ABNT.", "benefit": "Segurança contra o uso de normas desatualizadas."},
            {"title": "NBR 15575 de Desempenho", "desc": "Checklists e orientações rigorosas sobre vida útil de projeto (VUP), desempenho acústico, térmico e lumínico de edificações.", "benefit": "Adequação completa a exigências habitacionais."},
            {"title": "Normas de Segurança (NRs)", "desc": "Consulte regras de segurança de canteiro de obras (NR-18, NR-35 e outras) para reduzir riscos jurídicos e operacionais.", "benefit": "Conformidade física e jurídica garantida no canteiro."}
        ],
        "steps": [
            {"step": "1", "title": "Escolha o Tema Técnico", "desc": "Defina o tema da dúvida técnica (ex: acessibilidade de rampa, taxa de armadura, desempenho acústico)."},
            {"step": "2", "title": "Indique a Norma (Opcional)", "desc": "Opcionalmente, especifique a NBR que deseja focar (ex: NBR 9050, NBR 6118, NBR 15575)."},
            {"step": "3", "title": "Processamento da IA", "desc": "O NormaMatch PRO busca em sua base de conhecimento e na web as exigências exatas vigentes."},
            {"step": "4", "title": "Aplique a Resolução", "desc": "Copie os parâmetros normativos recomendados para o seu memorial descritivo, projeto ou relatório técnico."}
        ],
        "prompts": [
            {
                "name": "Verificação de Coeficientes",
                "objective": "Consultar coeficientes de ponderação e limites estruturais.",
                "instruction": "Você é o NormaMatch PRO. Quais são os coeficientes de majoração de cargas e minoração de resistência estabelecidos pela NBR 6118 para verificação de estados limites últimos em estruturas de concreto armado convencionais?",
                "placeholders": "Nenhum campo necessário"
            },
            {
                "name": "Cobrimento de Armadura por Classe",
                "objective": "Identificar o cobrimento mínimo exigido conforme a agressividade ambiental.",
                "instruction": "Você é o NormaMatch PRO. Qual o cobrimento nominal mínimo de armadura exigido para pilares de concreto armado em ambiente com Classe de Agressividade Ambiental [CLASSE] conforme a NBR 6118?",
                "placeholders": "[CLASSE] (ex: III - Forte)"
            },
            {
                "name": "Exigências de Desempenho Acústico",
                "objective": "Enquadrar os limites de isolamento acústico entre unidades habitacionais.",
                "instruction": "Você é o NormaMatch PRO. Quais são as exigências mínimas e métodos de avaliação de desempenho acústico estabelecidos pela NBR 15575 para paredes divisórias entre unidades habitacionais autônomas (dormitório/dormitório e dormitório/sala)?",
                "placeholders": "Nenhum campo necessário"
            },
            {
                "name": "Rampa de Acessibilidade (NBR 9050)",
                "objective": "Dimensionar inclinações máximas de rampas acessíveis.",
                "instruction": "Você é o NormaMatch PRO. Com base nas exigências da NBR 9050, determine a inclinação admissível e o dimensionamento correto para uma rampa de acessibilidade que vence um desnível de [DESNIVEL] metros. Indique a quantidade de patamares necessários.",
                "placeholders": "[DESNIVEL] (ex: 1.2)"
            }
        ],
        "benefits": [
            "Agilidade de Pesquisa: Economize horas de folheação de normas gigantescas.",
            "Conformidade Garantida: Reduza o risco de reprovação de projetos em órgãos fiscalizadores.",
            "Embasamento Profissional: Justifique suas decisões de projeto citando artigos específicos das NBRs."
        ],
        "for_whom": [
            "Projetistas e Arquitetos: que precisam especificar materiais e layouts de acordo com as normas.",
            "Engenheiros Calculistas e de Fundações: que devem seguir rigorosamente a NBR 6118 e NBR 6122.",
            "Peritos e Auditores: que necessitam de embasamento normativo sólido para emitir laudos incontestáveis."
        ],
        "included": [
            "Acesso imediato ao agente NormaMatch PRO no Google Gemini.",
            "4 prompts de consulta e checklist técnico baseados nas principais NBRs.",
            "Guia de bolso digital para navegação de normas de engenharia.",
            "Atualizações periódicas alinhadas às revisões da ABNT."
        ],
        "faq": [
            {"q": "O NormaMatch PRO tem acesso ao texto completo de todas as NBRs?", "a": "O agente possui uma ampla base de conhecimento sobre as principais NBRs da construção civil e está conectado ao Google Search para buscar dados atualizados, mas recomenda-se sempre confrontar dados críticos com as normas adquiridas formalmente na ABNT."},
            {"q": "Ele pode ajudar em processos de certificação PBQP-H?", "a": "Sim, fornecendo checklists de conformidade técnica, requisitos de controle de qualidade e validação de procedimentos em conformidade com as normas do SiAC/PBQP-H."},
            {"q": "O agente ajuda a elaborar justificativas para laudos técnicos?", "a": "Com certeza. Ele ajuda a redigir fundamentações técnicas impecáveis, citando os itens específicos e exigências das normas aplicáveis."},
            {"q": "Como a IA lida com normas que foram atualizadas recentemente?", "a": "O agente utiliza pesquisa web ativa (Google Search) integrada no Gemini para cruzar as informações da sua base com as notícias e atualizações mais recentes do portal de catálogo da ABNT."},
            {"q": "As respostas do agente podem ser usadas diretamente em laudos judiciais?", "a": "O agente ajuda na redação e na pesquisa dos itens normativos, mas as respostas devem ser revisadas e assinadas por um engenheiro devidamente registrado no CREA com emissão de ART."},
            {"q": "Ele abrange também normas internacionais como ASTM ou Eurocode?", "a": "O foco principal do NormaMatch PRO são as normas brasileiras (ABNT NBR) e as Normas Regulamentadoras (NR) do Ministério do Trabalho, mas ele pode realizar pesquisas comparativas com padrões internacionais se solicitado."},
            {"q": "O agente necessita de instalação local?", "a": "Não. O agente roda em nuvem através da plataforma Google Gemini. Você recebe o link de configuração oficial para uso imediato."},
            {"q": "Como funciona o suporte pós-compra?", "a": "Oferecemos suporte por e-mail e canal de dúvidas para ajudar você a obter o máximo desempenho nas suas consultas de prompts."}
        ]
    },
    {
        "filename": "analise-edital-licitacao-ia.html",
        "gem_number": "GEM 06",
        "name": "LegalMatch PRO",
        "category": "Licitações e Contratos",
        "keyword": "ia para licitacoes",
        "title": "LegalMatch PRO | IA para Licitações e Análise de Editais",
        "meta_desc": "Analise editais de obras, identifique riscos jurídicos, monte justificativas técnicas e minutas de recursos sob a Nova Lei de Licitações (Lei 14.133) com IA.",
        "short_desc": "Blindagem jurídica e inteligência administrativa para editais de obras públicas sob a Lei 14.133/2021 e orientações do TCU.",
        "gemini_link": "https://gemini.google.com/gem/17hhJkiI1p9uItxf5pOWpq3ltqDIN0K1U?usp=sharing",
        "emoji": "⚖️",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Analise Editais e Impugne Cláusulas Abusivas sob a Lei 14.133",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <line x1="12" y1="4" x2="12" y2="20"/><line x1="6" y1="20" x2="18" y2="20"/><line x1="5" y1="7" x2="19" y2="7"/>
                <path d="M5 7l-2.5 6a3 3 0 005 0z"/><path d="M19 7l-2.5 6a3 3 0 005 0z"/>
            </svg>
        """,
        "problem_now": "A participação ineficiente em licitações de obras públicas envolve um cipoal jurídico e burocrático. Editais frequentemente contêm exigências de qualificação técnica abusivas ou ilegais, prazos inexequíveis e matrizes de riscos desbalanceadas que transferem toda a responsabilidade de imprevistos geológicos ou climáticos para a construtora, resultando em inabilitações injustas ou contratos deficitários.",
        "transformation": "Com o LegalMatch PRO, você analisa editais inteiros em minutos. O agente identifica pontos críticos, restrições à competitividade e cláusulas em desacordo com a Lei 14.133/2021 e decisões do TCU. Ele redige minutas de impugnação sólidas, pedidos de esclarecimento estruturados e defesas técnicas contra inabilitações injustas com rapidez e rigor jurídico.",
        "features": [
            {"title": "Análise de Riscos em Editais", "desc": "Faz uma varredura completa em editais de licitação, identificando exigências abusivas, restrições e riscos de engenharia.", "benefit": "Evita assumir contratos com armadilhas financeiras."},
            {"title": "Minutas de Recursos e Impugnações", "desc": "Escreve minutas robustas para recursos administrativos ou impugnações fundamentadas de acordo com a Nova Lei de Licitações (Lei 14.133).", "benefit": "Agilidade em contestações legais urgentes."},
            {"title": "Equilíbrio Econômico-Financeiro", "desc": "Auxilia na fundamentação de pedidos de reequilíbrio, reajuste ou revisão contratual devido a oscilações de insumos ou imprevistos.", "benefit": "Preservação da margem de lucro em contratos de longo prazo."},
            {"title": "Conformidade com Acórdãos do TCU", "desc": "Cruza exigências de editais com a jurisprudência mais atualizada do Tribunal de Contas da União para garantir conformidade.", "benefit": "Segurança embasada no órgão fiscalizador máximo."}
        ],
        "steps": [
            {"step": "1", "title": "Insira o Trecho do Edital", "desc": "Copie e cole os capítulos de qualificação técnica, habilitação ou a matriz de riscos do edital sob análise."},
            {"step": "2", "title": "Defina o Objetivo da Análise", "desc": "Escolha se deseja mapear riscos contratuais, redigir impugnação técnica ou montar recurso contra inabilitação."},
            {"step": "3", "title": "Execução da IA", "desc": "O LegalMatch PRO analisa os dados em conformidade com a Lei 14.133/2021 e jurisprudências do TCU."},
            {"step": "4", "title": "Obtenha a Minuta Jurídica", "desc": "Copie a minuta gerada, ajuste os dados da sua empresa e dê entrada no processo licitatório com segurança."}
        ],
        "prompts": [
            {
                "name": "Identificação de Cláusulas Abusivas",
                "objective": "Analisar cláusulas restritivas de qualificação técnica.",
                "instruction": "Você é o LegalMatch PRO. Analise este trecho do edital de licitação: [TRECHO_EDITAL]. Verifique se a exigência de [EXIGENCIA] (ex: atestados limitados a tempo ou quantidade) possui respaldo legal na Nova Lei de Licitações (Lei 14.133/2021) e aponte acórdãos do TCU que condenem tal restrição.",
                "placeholders": "[TRECHO_EDITAL] (Cole o capítulo de qualificação técnica), [EXIGENCIA] (ex: registro no CREA regional na data de abertura)"
            },
            {
                "name": "Minuta de Impugnação ao Edital",
                "objective": "Escrever uma peça administrativa para questionar o edital.",
                "instruction": "Você é o LegalMatch PRO. Redija uma minuta de impugnação técnica direcionada à comissão de licitação do edital de número [NUMERO_EDITAL], argumentando detalhadamente contra a exigência abusiva de [EXIGENCIA_ABUSIVA], fundamentando no Artigo 67 da Lei 14.133/2021 e jurisprudências correlatas.",
                "placeholders": "[NUMERO_EDITAL] (ex: Tomada de Preços 02/2024), [EXIGENCIA_ABUSIVA] (ex: atestado com mais de 70% do quantitativo da obra)"
            },
            {
                "name": "Pedido de Reequilíbrio Econômico",
                "objective": "Fundamentar a revisão de preços do contrato por oscilação de insumos.",
                "instruction": "Você é o LegalMatch PRO. Redija a fundamentação técnica e jurídica para um pedido de reequilíbrio econômico-financeiro de contrato de obra pública, alegando o aumento imprevisível de [INSUMO] em [PERCENTUAL]% verificado entre a data da proposta e a data atual, citando o Artigo 124 da Lei 14.133/2021.",
                "placeholders": "[INSUMO] (ex: aço CA-50), [PERCENTUAL] (ex: 35)"
            },
            {
                "name": "Recurso contra Inabilitação Técnica",
                "objective": "Contestar a desclassificação injusta por suposta falta de acervo.",
                "instruction": "Você é o LegalMatch PRO. Elabore uma minuta de recurso administrativo contra a decisão de inabilitação da construtora [NOME_EMPRESA], no Edital [EDITAL], motivada pelo suposto não atendimento da exigência de comprovação de experiência em [SERVICO_QUESTIONADO]. Demonstre que o atestado de acervo técnico (CAT) apresentado atende plenamente ao princípio da equivalência técnica.",
                "placeholders": "[NOME_EMPRESA] (sua empresa), [EDITAL] (ex: Concorrência 10/2024), [SERVICO_QUESTIONADO] (ex: execução de contenção em cortina atirantada)"
            }
        ],
        "benefits": [
            "Blindagem Contratual: Evite assinar contratos de obras públicas com cláusulas prejudiciais à saúde da empresa.",
            "Economia de Custos Legais: Esboce petições e minutas complexas sem precisar depender de assessoria jurídica terceirizada a todo momento.",
            "Competitividade Acentuada: Combata inabilitações arbitrárias de concorrentes ou de comissões despreparadas."
        ],
        "for_whom": [
            "Empresas de Engenharia Licitantes: que participam ativamente de pregões e concorrências públicas.",
            "Engenheiros e Diretores de Construtoras: que assinam contratos e gerenciam as relações de fiscalização com órgãos públicos.",
            "Advogados e Assessores Jurídicos da Área de Infraestrutura: que desejam acelerar a pesquisa de jurisprudência do TCU."
        ],
        "included": [
            "Acesso imediato ao agente LegalMatch PRO no Google Gemini.",
            "4 prompts de alto impacto para análise contratual e impugnações.",
            "Modelos prontos de estrutura de petição administrativa de licitação.",
            "Atualizações e melhorias alinhadas às novas resoluções do PNCP."
        ],
        "faq": [
            {"q": "O LegalMatch PRO é atualizado com a Nova Lei de Licitações (Lei 14.133)?", "a": "Sim. O agente foi totalmente calibrado de acordo com a Lei 14.133/2021, jurisprudência do TCU e PNCP (Portal Nacional de Contratações Públicas)."},
            {"q": "Consigo analisar editais em formato PDF?", "a": "Sim. Você pode fazer upload do edital em PDF diretamente no Google Gemini (disponível na interface) e o agente fará a leitura e análise completa das seções indicadas."},
            {"q": "Ele serve também para elaboração de Termos de Referência?", "a": "Com certeza. O agente auxilia gestores públicos a estruturarem Termos de Referência (TR) e especificações técnicas de forma clara e blindada juridicamente."},
            {"q": "O agente emite laudos jurídicos formais?", "a": "Não. O agente gera minutas, pareceres e orientações de apoio técnico e jurisprudencial. A decisão final de peticionar e a assinatura das peças são de responsabilidade do profissional de engenharia ou do advogado da empresa."},
            {"q": "Como funciona o cruzamento com acórdãos do TCU?", "a": "O agente utiliza sua base interna integrada com a pesquisa do Google Search em tempo real para encontrar as deliberações e acórdãos mais recentes do Tribunal de Contas da União sobre licitações de obras."},
            {"q": "Ele pode ser usado para licitações municipais e estaduais?", "a": "Sim. Como a Lei 14.133/2021 é de caráter nacional, o agente atende perfeitamente a licitações em esferas municipal, estadual e federal, além de considerar particularidades estaduais quando fornecidas."},
            {"q": "O agente armazena os dados dos editais que eu envio?", "a": "Não. As interações são efetuadas sob a política de privacidade e segurança da sua conta no Google Gemini, garantindo que os seus documentos internos e editais não fiquem expostos."},
            {"q": "Posso utilizá-lo para contestar multas contratuais com órgãos públicos?", "a": "Sim. Ele ajuda a estruturar a defesa fundamentada demonstrando causas excludentes de responsabilidade, como atrasos motivados pela própria administração ou chuvas atípicas."}
        ]
    },
    {
        "filename": "laudo-vistoria-cautelar-patologias-ia.html",
        "gem_number": "GEM 07",
        "name": "LaudoMatch PRO",
        "category": "Engenharia Diagnóstica",
        "keyword": "ia laudo de vistoria cautelar",
        "title": "LaudoMatch PRO | IA para Laudo de Vistoria Cautelar e Patologias",
        "meta_desc": "Elabore laudos de vistoria cautelar de vizinhança, laudos de patologia predial e perícias técnicas em conformidade com as normas ABNT NBR utilizando IA.",
        "short_desc": "Estrutura e diagnósticos técnicos para engenharia diagnóstica, laudos de patologia predial, perícias judiciais e vistorias cautelares.",
        "gemini_link": "https://gemini.google.com/gem/1gZNu_M9sIGB59VHy_2XVWRAVxufO7kra?usp=sharing",
        "emoji": "🔍",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Laudos de Vistoria e Diagnósticos de Patologias com Rigor Técnico",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3a1 1 0 011-1h4a1 1 0 011 1v1"/><path d="M8.5 12.5l2 2 4-4"/>
            </svg>
        """,
        "problem_now": "A engenharia diagnóstica requer uma riqueza de detalhes minuciosa e termos precisos. Redigir laudos de vistoria cautelar de vizinhança ou classificar anomalias prediais manualmente gera dias de trabalho burocrático. Além disso, classificar erroneamente uma fissura estrutural como mera fissura de reboco ou deixar de citar as exigências da NBR 13752 e NBR 16747 abre brechas para questionamentos judiciais e prejuízos imensos.",
        "transformation": "Com o LaudoMatch PRO, você acelera a montagem dos seus laudos. O agente ajuda a classificar anomalias (endógenas, exógenas) e falhas, sugere ensaios tecnológicos apropriados e prescreve métodos de recuperação corretos. Graças ao suporte a imagens do Gemini, você pode analisar fotos de patologias (trincas, corrosão de armadura, infiltrações) e obter pré-diagnósticos imediatos e fundamentação normativa impecável.",
        "features": [
            {"title": "Engenharia Diagnóstica Estruturada", "desc": "Estrutura laudos técnicos, vistorias cautelares de vizinhança e inspeções de manutenção em conformidade com as normas vigentes.", "benefit": "Laudos padronizados e aceitos pelo mercado e justiça."},
            {"title": "Inspeção Predial (NBR 16747:2020)", "desc": "Auxilia na classificação sistemática de anomalias (endógenas, exógenas) e falhas, organizando por grau de prioridade técnica.", "benefit": "Clareza operacional na definição de prioridades do condomínio."},
            {"title": "Perícias Judiciais (NBR 13752)", "desc": "Ajuda peritos e assistentes técnicos a formatarem petições, laudos periciais e a responderem a quesitos técnicos judiciais com rigor.", "benefit": "Segurança no trabalho pericial perante o juízo."},
            {"title": "Análise Visual de Patologias", "desc": "Envie fotos de fissuras, infiltrações ou corrosão e obtenha pré-diagnósticos técnicos detalhados e causas prováveis.", "benefit": "Diagnósticos iniciais ágeis baseados em imagens claras."}
        ],
        "steps": [
            {"step": "1", "title": "Descreva a Manifestação Patológica", "desc": "Descreva as características visuais da anomalia (ou anexe fotos da trinca, infiltração ou oxidação estrutural)."},
            {"step": "2", "title": "Indique a Metodologia de Inspeção", "desc": "Indique o tipo de laudo desejado: Vistoria Cautelar, Inspeção Predial NBR 16747 ou Laudo Pericial Judicial."},
            {"step": "3", "title": "Processamento do Diagnóstico", "desc": "O LaudoMatch PRO pesquisa causas prováveis, termos científicos exatos e normas aplicáveis."},
            {"step": "4", "title": "Gere e Entregue o Laudo", "desc": "Copie o texto estruturado com diagnóstico e diretrizes de reparo, insira seu registro profissional (CREA) e emita a ART."}
        ],
        "prompts": [
            {
                "name": "Estrutura de Laudo de Vistoria Cautelar",
                "objective": "Gerar o escopo e seções obrigatórias para vistoria de vizinhança.",
                "instruction": "Você é o LaudoMatch PRO. Monte a estrutura técnica completa e o roteiro de inspeção para um Laudo de Vistoria Cautelar de Vizinhança para um imóvel residencial térreo que faz divisa com um terreno onde será executada uma obra de edifício com [PROFUNDIDADE_ESCAVACAO] metros de escavação e contenção em parede diafragma.",
                "placeholders": "[PROFUNDIDADE_ESCAVACAO] (ex: 6)"
            },
            {
                "name": "Classificação e Diagnóstico de Fissuras",
                "objective": "Classificar anomalias físicas e propor a causa provável.",
                "instruction": "Você é o LaudoMatch PRO. Analise a seguinte descrição de anomalia: [DESCRICAO_ANOMALIA] localizada em [LOCALIZACAO]. Classifique o fenômeno técnico (anomalia endógena, exógena, funcional), a gravidade ou urgência da manutenção conforme a NBR 16747 e apresente as causas prováveis e sugestão de ensaios complementares.",
                "placeholders": "[DESCRICAO_ANOMALIA] (ex: trincas a 45 graus partindo dos cantos das janelas), [LOCALIZACAO] (ex: fachada de alvenaria estrutural)"
            },
            {
                "name": "Resposta a Quesitos Judiciais",
                "objective": "Redigir a resposta técnica formal de quesito formulado pelo juiz ou partes.",
                "instruction": "Você é o LaudoMatch PRO. Redija a resposta pericial técnica, formal e embasada cientificamente para o seguinte quesito judicial: [QUESITO_JUDICIAL]. Considere que a perícia versa sobre [TIPO_PERICIA] em condomínio edilício e fundamente conforme a NBR 13752.",
                "placeholders": "[QUESITO_JUDICIAL] (ex: Se a umidade constatada no subsolo provém de vazamento na rede de águas pluviais ou de falha de impermeabilização), [TIPO_PERICIA] (ex: vício construtivo e infiltração)"
            },
            {
                "name": "Memorial de Recuperação Estrutural",
                "objective": "Especificar o método de tratamento de armaduras corroídas.",
                "instruction": "Você é o LaudoMatch PRO. Elabore a especificação técnica e o passo a passo de procedimentos para a recuperação de uma viga de concreto armado com [PATOLOGIA_CONCRETO] (ex: armadura exposta com corrosão acentuada e perda de seção). Indique materiais de reparo, tratamento das barras e etapas de cura.",
                "placeholders": "[PATOLOGIA_CONCRETO] (ex: cobrimento desplacado, oxidação acentuada das armaduras e estribos rompidos)"
            }
        ],
        "benefits": [
            "Terminologia Científica: Laudos redigidos com termos específicos da engenharia diagnóstica (concreto, patologia).",
            "Diretrizes de Manutenção: Indicação de procedimentos de reparo adequados conforme as boas práticas do IBAPE.",
            "Rigor Normativo: Redução de contestações judiciais de laudos devido a falhas conceituais ou falta de referências técnicas."
        ],
        "for_whom": [
            "Peritos de Engenharia e Assistentes Técnicos: que atuam em disputas judiciais de vícios construtivos ou danos de vizinhança.",
            "Síndicos e Administradores de Condomínio: que necessitam de pareceres para contratar obras de manutenção estrutural.",
            "Construtores e Empreiteiros: que realizam reformas e necessitam registrar as condições de imóveis vizinhos antes de iniciar a obra."
        ],
        "included": [
            "Acesso imediato ao agente LaudoMatch PRO no Google Gemini.",
            "4 prompts avançados para vistorias, diagnósticos e respostas judiciais.",
            "Guia de bolso de termos periciais e códigos de engenharia diagnóstica.",
            "Atualizações técnicas constantes integradas ao desenvolvimento de IA."
        ],
        "faq": [
            {"q": "O LaudoMatch PRO consegue analisar fotos de rachaduras ou infiltrações?", "a": "Sim. Graças à capacidade multimodal do Gemini, você pode carregar imagens de patologias da construção diretamente no chat. O agente avalia as características visuais e propõe causas e soluções."},
            {"q": "O laudo gerado segue as normas da ABNT?", "a": "Sim, a redação e estrutura são orientadas pelas principais normas vigentes de engenharia diagnóstica, como a NBR 13752 (Perícias de Engenharia na Construção Civil) e NBR 16747 (Inspeção Predial)."},
            {"q": "Ele auxilia na emissão da ART?", "a": "O agente orienta sobre a correta classificação de atividades e seleção de códigos TOS na emissão da Anotação de Responsabilidade Técnica (ART) do laudo junto ao CREA."},
            {"q": "Como funciona o upload de fotos no Gemini?", "a": "Na interface do Google Gemini (no computador ou celular), você clica no ícone de anexo de imagem '+', seleciona a foto da patologia em alta resolução e cola o prompt correspondente para análise."},
            {"q": "O agente substitui a vistoria presencial?", "a": "De forma alguma. A vistoria física é indispensável e obrigatória para atestar a realidade do imóvel. O agente funciona na retaguarda, ajudando a organizar e fundamentar os dados levantados em campo."},
            {"q": "Ele classifica danos de acordo com as normas de seguro predial?", "a": "Sim. Você pode pedir para o agente estruturar a análise para verificar se a anomalia se enquadra nas coberturas de danos de sinistros ou falhas decorrentes de falta de manutenção predial."},
            {"q": "Qual é a velocidade de geração de um laudo pericial?", "a": "Em menos de 2 minutos você obtém a fundamentação teórica, a estrutura e a indicação metodológica para o laudo. O preenchimento dos detalhes específicos da vistoria é feito em seguida pelo profissional."},
            {"q": "É cobrada alguma taxa mensal pelo uso do agente?", "a": "Não. O acesso aos prompts e à configuração do especialista é vitalício após o pagamento único do pacote Agentes Match."}
        ]
    },
    {
        "filename": "diario-obra-rdo-checklist-ia.html",
        "gem_number": "GEM 04",
        "name": "MatchObra PRO",
        "category": "Gestão de Obras",
        "keyword": "diario de obra automatizado ia",
        "title": "MatchObra PRO | IA para Diário de Obra e Checklist de Qualidade",
        "meta_desc": "Automatize o preenchimento de Diários de Obra (RDO), checklists de controle de qualidade (FVS) e monitoramento de canteiro com Inteligência Artificial.",
        "short_desc": "Supervisor técnico virtual: RDO automático, checklists de qualidade baseados na NBR 15575 e conformidade de segurança (NR-18).",
        "gemini_link": "https://gemini.google.com/gem/1mV7RNTqWI6eUaPf5ibK3OkXk6yw4qWc-?usp=sharing",
        "emoji": "🏢",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Diários de Obra (RDO) e Checklists de Qualidade sem Burocracia",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <rect x="4" y="10" width="8" height="11"/><rect x="6.3" y="13" width="1.6" height="1.6"/><rect x="8.9" y="13" width="1.6" height="1.6"/>
                <rect x="6.3" y="16.5" width="1.6" height="1.6"/><rect x="8.9" y="16.5" width="1.6" height="1.6"/>
                <path d="M15 21V6h1l4 1"/><line x1="15" y1="9" x2="20" y2="9"/><line x1="18" y1="9" x2="18" y2="11"/>
            </svg>
        """,
        "problem_now": "Manter o Diário de Obra (RDO) atualizado e preencher Fichas de Verificação de Serviço (FVS) consome tempo que o engenheiro deveria estar usando para coordenar as frentes de trabalho. A burocracia de relatórios diários de canteiro, aliada à necessidade de fiscalizar as regras da NR-18 e NBR 12655 (concreto) gera atrasos, esquecimentos e deixa a construtora vulnerável a processos trabalhistas ou retrabalhos técnicos.",
        "transformation": "Com o MatchObra PRO, você automatiza a gestão física do seu canteiro. Ao transcrever anotações rápidas ou áudios gravados no WhatsApp pelo celular, o agente formata um Diário de Obra completo estruturado em minutos. Ele gera checklists de FVS e auditorias de NR-18 customizadas por tipo de serviço, garantindo que o controle tecnológico e a segurança do trabalho estejam sempre documentados.",
        "features": [
            {"title": "Diário de Obra Rápido (RDO)", "desc": "Gera relatórios diários de obra estruturados contendo clima, efetivo de pessoal, atividades executadas, ocorrências e recebimento de materiais.", "benefit": "RDO completo e organizado com gravação rápida."},
            {"title": "Fichas de Verificação de Serviço", "desc": "Checklists de qualidade (FVS) baseados nas normas brasileiras para controle tecnológico (NBR 12655 - Concreto, NBR 15575 - Desempenho).", "benefit": "Controle tecnológico rígido e facilidade de auditoria."},
            {"title": "Auditor de NR-18 e Canteiro", "desc": "Identifica riscos físicos ou procedimentais em fotos e relata não conformidades com base nas normas regulamentadoras de segurança.", "benefit": "Canteiro seguro e redução de riscos trabalhistas."},
            {"title": "Planejamento e Acompanhamento", "desc": "Organiza listas de tarefas semanais e identifica gargalos e caminho crítico na execução física para evitar atrasos.", "benefit": "Controle de prazos e fluxo de obra fluído."}
        ],
        "steps": [
            {"step": "1", "title": "Envie os Registros Diários", "desc": "Insira ou fale os dados do dia: clima, subempreiteiros ativos, materiais recebidos e atividades concluídas."},
            {"step": "2", "title": "Selecione o Controle", "desc": "Escolha se deseja formatar o RDO técnico do dia ou gerar uma ficha de controle tecnológico de concreto/FVS."},
            {"step": "3", "title": "Geração do Relatório", "desc": "O MatchObra PRO compila os registros de forma profissional, padronizada e limpa."},
            {"step": "4", "title": "Arquivamento e Compartilhamento", "desc": "Salva o diário formatado no arquivo da construtora ou envie em PDF diretamente ao cliente."}
        ],
        "prompts": [
            {
                "name": "Elaboração de Diário de Obra (RDO)",
                "objective": "Compilar notas avulsas em um RDO formal técnico.",
                "instruction": "Você é o MatchObra PRO. Elabore um Relatório Diário de Obra (RDO) estruturado com base nas seguintes informações de campo: Clima: [CLIMA]. Efetivo: [EFETIVO]. Atividades do dia: [ATIVIDADES]. Ocorrências relevantes: [OCORRENCIAS]. Organize em seções: Condições Climáticas, Efetivo de Mão de Obra, Serviços Executados, Recebimento de Materiais e Ocorrências.",
                "placeholders": "[CLIMA] (ex: nublado com chuva à tarde), [EFETIVO] (ex: 12 serventes, 6 pedreiros, 2 encanadores), [ATIVIDADES] (ex: execução de formas e concretagem dos pilares do 4º pavimento)"
            },
            {
                "name": "Ficha de Verificação de Serviço (FVS)",
                "objective": "Criar checklist de controle de qualidade para uma etapa específica.",
                "instruction": "Você é o MatchObra PRO. Crie uma Ficha de Verificação de Serviço (FVS) detalhada para a atividade de [SERVICO_QUALIDADE]. O checklist deve abranger verificações 'Antes da Execução', 'Durante a Execução' e 'Após a Execução', citando as referências normativas brasileiras vigentes.",
                "placeholders": "[SERVICO_QUALIDADE] (ex: impermeabilização de laje de cobertura com manta asfáltica)"
            },
            {
                "name": "Conformidade NR-18 (Segurança)",
                "objective": "Criar roteiro de inspeção de segurança para trabalho específico.",
                "instruction": "Você é o MatchObra PRO. Quais são as exigências de proteção coletiva e individual de segurança previstas na NR-18 e NR-35 que devem ser inspecionadas e atendidas obrigatoriamente antes de liberar o serviço de [SERVICO_RISCO] no canteiro?",
                "placeholders": "[SERVICO_RISCO] (ex: reboco de fachada externa em balancim suspenso)"
            },
            {
                "name": "Diálogo Diário de Segurança (DDS)",
                "objective": "Redigir o texto do treinamento rápido de segurança do canteiro.",
                "instruction": "Você é o MatchObra PRO. Escreva um texto persuasivo e instrutivo para um Diálogo Diário de Segurança (DDS) focado na importância de [TEMA_DDS], direcionado para pedreiros, ajudantes e carpinteiros de obra residencial de edifícios.",
                "placeholders": "[TEMA_DDS] (ex: uso de proteção facial em lixamento de concreto e proteção coletiva em aberturas de lajes)"
            }
        ],
        "benefits": [
            "Canteiro Documentado: Histórico completo e detalhado do dia a dia da obra para resguardo legal da empresa.",
            "Padronização de Qualidade: Checklists claros que ajudam a equipe de mestres e encarregados a evitar falhas construtivas.",
            "Economia de Tempo de Escritório: Fechamento rápido de relatórios que antes levavam horas no final do dia."
        ],
        "for_whom": [
            "Engenheiros Residentes e Fiscais de Obra: que respondem diretamente pela qualidade e documentação de campo.",
            "Técnicos em Segurança do Trabalho: que fiscalizam os canteiros e aplicam checklists de prevenção.",
            "Construtores e Empreiteiros: que precisam dar report diário e transparente do progresso físico ao cliente."
        ],
        "included": [
            "Acesso imediato ao agente MatchObra PRO no Google Gemini.",
            "4 prompts calibrados para diários de obra, FVS, DDS e NR-18.",
            "Guia digital para documentação ágil de canteiros de obras.",
            "Atualizações tecnológicas integradas de IA no gerenciamento de obras."
        ],
        "faq": [
            {"q": "Como o MatchObra PRO agiliza o preenchimento do RDO?", "a": "Você pode enviar anotações rápidas por texto, ou mesmo transcrição de áudios feitos no canteiro pelo celular, e o agente organiza tudo em um documento técnico e limpo pronto para arquivar."},
            {"q": "Ele ajuda no controle tecnológico do concreto?", "a": "Sim, auxiliando na conferência de dados de ensaios de corpos de prova (fck), prazos de desforma e cuidados durante o processo de cura úmida conforme a NBR 14931."},
            {"q": "O agente funciona offline?", "a": "O agente roda através do Google Gemini e requer acesso à internet. No entanto, você pode estruturar modelos de planilhas e checklists pelo agente para usar offline em campo no celular."},
            {"q": "Posso transcrever áudio do WhatsApp direto no agente?", "a": "Sim. Você pode utilizar a ferramenta de digitação por voz do teclado do seu smartphone ou transcrever o áudio gravado no canteiro e colar no chat do Gemini para o agente estruturar."},
            {"q": "O agente emite o RDO em PDF diretamente?", "a": "Ele gera o texto do RDO perfeitamente formatado. Você pode copiá-lo e colá-lo em um arquivo do Word ou Google Docs e salvar em PDF com apenas dois cliques."},
            {"q": "A FVS gerada atende à certificação PBQP-H?", "a": "Sim. Como a estrutura da FVS mapeia as verificações normativas por etapas (antes, durante e após), ela é perfeitamente adequada para compor a documentação de qualidade exigida pelo PBQP-H e ISO 9001."},
            {"q": "Ele identifica riscos de segurança por foto do canteiro?", "a": "Se você utilizar a version multimodal do Gemini e fizer o upload da foto do canteiro, o agente fará uma leitura visual apontando possíveis riscos de não conformidade com a NR-18."},
            {"q": "Como faço para comprar a suíte completa de agentes?", "a": "Basta clicar em qualquer botão de compra nesta página para ser direcionado ao checkout seguro e garantir o acesso vitalício a todos os 9 agentes."}
        ]
    },
    {
        "filename": "calculo-estrutural-dimensionamento-ia.html",
        "gem_number": "GEM 08",
        "name": "EstruturaMatch PRO",
        "category": "Cálculo Estrutural",
        "keyword": "ia calculo estrutural",
        "title": "EstruturaMatch PRO | IA para Dimensionamento e Cálculo Estrutural",
        "meta_desc": "Realize pré-dimensionamentos estruturais de concreto armado, vigas, pilares e sapatas em conformidade com as normas ABNT NBR utilizando IA.",
        "short_desc": "Dimensionamento e pré-dimensionamento de elementos estruturais (concreto, aço, madeira), reforços de patologias e análise da NBR 6118.",
        "gemini_link": "https://gemini.google.com/gem/10xfRN9InbZqg2rB4qZ09bd5o_5urYRST?usp=sharing",
        "emoji": "🏗️",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Pré-Dimensionamento Estrutural e Memoriais Rápidos de Concreto e Aço",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/>
                <line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/>
            </svg>
        """,
        "problem_now": "Realizar pré-dimensionamentos estruturais no início do projeto arquitetônico manualmente é trabalhoso. Os arquitetos precisam de respostas rápidas sobre a altura das vigas ou dimensões de pilares, e o engenheiro calculista gasta horas modelando no software estrutural apenas para fazer estimativas geométricas básicas ou calcular taxas mínimas de armaduras e sapatas.",
        "transformation": "Com o EstruturaMatch PRO, você resolve pré-dimensionamentos estruturais instantaneamente. O agente calcula a seção aproximada de vigas, pilares e sapatas de forma paramétrica seguindo a NBR 6118 (Concreto) e NBR 8800 (Metálicas). Ele gera memoriais de cálculo preliminares, auxilia a calcular comprimentos de ancoragem e propõe sistemas de reforço estrutural estruturados.",
        "features": [
            {"title": "Pré-Dimensionamento Rápido", "desc": "Calcula de forma rápida seções estimadas para vigas, pilares, lajes e sapatas em função das cargas e vãos de projeto.", "benefit": "Esboço e lançamento estrutural coerente em minutos."},
            {"title": "NBR 6118 de Concreto Armado", "desc": "Verificação de conformidade de cobrimentos, domínios de deformação, taxa mínima de armaduras e cálculo de flexão simples.", "benefit": "Segurança contra erros conceituais de dimensionamento."},
            {"title": "Análise de Patologias Estruturais", "desc": "Auxilia na identificação de causas de fissuras, deformações excessivas ou corrosão de armaduras em elementos estruturais existentes.", "benefit": "Direcionamento técnico rápido de soluções de reforço."},
            {"title": "Comparação de Sistemas", "desc": "Avalia o impacto financeiro e arquitetônico comparando concreto armado convencional, alvenaria estrutural e concreto protendido.", "benefit": "Decisões de engenharia assertivas e econômicas."}
        ],
        "steps": [
            {"step": "1", "title": "Indique os Parâmetros", "desc": "Forneça o vão do elemento, cargas aplicadas (permanentes e variáveis) e as propriedades do material (fck do concreto, classe do aço)."},
            {"step": "2", "title": "Processamento e Verificação", "desc": "O EstruturaMatch PRO aplica as equações analíticas básicas da teoria de concreto armado ou perfis metálicos."},
            {"step": "3", "title": "Geração do Memorial", "desc": "O agente apresenta a seção estimada do elemento, área de aço mínima necessária e referências normativas."},
            {"step": "4", "title": "Modelagem Fina", "desc": "Você insere os dados pré-dimensionados no seu software de modelagem estrutural final (TQS, Eberick) para detalhamento fino."}
        ],
        "prompts": [
            {
                "name": "Cálculo de Flexão Simples (Viga)",
                "objective": "Calcular a área de aço necessária para flexão em viga de concreto.",
                "instruction": "Você é o EstruturaMatch PRO. Calcule a armadura longitudinal de tração para uma viga de concreto armado com seção retangular de [LARGURA] cm x [ALTURA] cm, submetida a um momento fletor de cálculo (Md) de [MOMENTO] kN.m. Considere fck de [FCK] MPa, aço CA-50 e cobrimento de [COBRIMENTO] cm.",
                "placeholders": "[LARGURA] (ex: 20), [ALTURA] (ex: 50), [MOMENTO] (ex: 120), [FCK] (ex: 30), [COBRIMENTO] (ex: 3.0)"
            },
            {
                "name": "Pré-Dimensionamento de Sapata Isolada",
                "objective": "Estimar a área da base de uma sapata baseada na carga do pilar.",
                "instruction": "Você é o EstruturaMatch PRO. Faça o pré-dimensionamento geométrico (largura e comprimento da base) de uma sapata isolada para um pilar de seção [DIMENSAO_PILAR] cm que descarrega uma carga vertical em serviço de [CARGA] kN, sabendo que a tensão admissível do solo é de [TENSAO_SOLO] kPa.",
                "placeholders": "[DIMENSAO_PILAR] (ex: 30x30), [CARGA] (ex: 800), [TENSAO_SOLO] (ex: 150)"
            },
            {
                "name": "Comprimento de Ancoragem de Barras",
                "objective": "Calcular o comprimento de ancoragem de barras de aço no concreto.",
                "instruction": "Você é o EstruturaMatch PRO. Determine o comprimento de ancoragem básico e necessário (com e sem gancho) para barras de diâmetro [DIAMETRO] mm de aço CA-50 tracionadas, em uma região de [ADESAOO] (boa ou má aderência), imersas em concreto com fck de [FCK] MPa.",
                "placeholders": "[DIAMETRO] (ex: 12.5), [ADESAOO] (ex: boa aderência), [FCK] (ex: 25)"
            },
            {
                "name": "Pré-Dimensionamento de Vigas de Aço",
                "objective": "Estimar a seção de perfil laminado I metálico.",
                "instruction": "Você é o EstruturaMatch PRO. Faça o pré-dimensionamento de uma viga biapoiada em perfil metálico tipo I laminado, vencendo um vão de [VAO] metros, sob uma carga distribuída de serviço de [CARGA_DISTRIBUIDA] kN/m. Siga as diretrizes de deflexão máxima (flecha) da NBR 8800.",
                "placeholders": "[VAO] (ex: 6.0), [CARGA_DISTRIBUIDA] (ex: 15)"
            }
        ],
        "benefits": [
            "Respostas Rápidas: Ideal para sanar dúvidas estruturais no canteiro de obras ou reuniões de compatibilização.",
            "Memoriais Didáticos: Demonstração do passo a passo matemático analítico para estudantes e engenheiros juniores.",
            "Rendimento Construtivo: Ajuda a escolher o sistema estrutural mais viável geometricamente no início do projeto."
        ],
        "for_whom": [
            "Engenheiros Civis Calculistas: que desejam realizar pré-dimensionamentos e conferir cálculos rápidos de vigas e pilares.",
            "Arquitetos e Urbanistas: que precisam de parâmetros geométricos coerentes para estruturar o projeto arquitetônico preliminar.",
            "Estudantes de Engenharia Civil: que necessitam de auxílio no aprendizado analítico das matérias de estruturas."
        ],
        "included": [
            "Acesso imediato ao agente EstruturaMatch PRO no Google Gemini.",
            "4 prompts estruturados para concreto armado, fundações e estruturas metálicas.",
            "Guia digital de fórmulas estruturais analíticas básicas.",
            "Atualizações futuras para novos elementos (madeira e alvenaria estrutural)."
        ],
        "faq": [
            {"q": "O EstruturaMatch PRO calcula estruturas inteiras de prédios?", "a": "Não. O agente serve para pré-dimensionamento de elementos isolados, auditoria de cálculos e auxílio de tomada de decisão técnica. Projetos estruturais completos devem ser modelados em softwares dedicados (TQS, Eberick) e detalhados por engenheiro especialista."},
            {"q": "Ele faz cálculo de estruturas de aço e madeira?", "a": "Sim, fornece diretrizes de dimensionamento seguindo a NBR 8800 (Aço) e NBR 7190 (Madeira)."},
            {"q": "Ele detalha o processo de cura do concreto?", "a": "Sim. O agente fornece todas as recomendações de desforma e cura úmida normatizadas pela NBR 14931."},
            {"q": "Como a IA consegue realizar contas matemáticas complexas?", "a": "Através dos algoritmos avançados do Google Gemini integrados com recursos de execução de códigos (code execution) no background, o agente resolve as equações com precisão decimal matemática."},
            {"q": "O agente emite desenhos de detalhamento técnico de ferragens?", "a": "Não. O agente gera as especificações de área de aço e seções de concreto textuais. O detalhamento gráfico de armaduras em prancha deve ser executado no CAD/BIM."},
            {"q": "Como posso integrar os resultados do agente no meu memorial estrutural?", "a": "Você pode copiar a memória de cálculo gerada pelo agente no Gemini e colá-la no seu editor de texto como memorial de pré-dimensionamento preliminar do projeto."},
            {"q": "Ele suporta verificação de vento e sismo conforme a NBR 6123?", "a": "O agente fornece os conceitos e roteiro de cálculo para cargas de vento, mas análises de pórticos espaciais complexos sob ação dinâmica devem ser efetuados em softwares dedicados."},
            {"q": "O pagamento é único ou recorrente?", "a": "O pagamento é único. Comprando a suíte de 9 agentes, você ganha acesso irrestrito e vitalício sem mensalidades."}
        ]
    },
    {
        "filename": "avaliacao-imoveis-imobiliaria-ia.html",
        "gem_number": "GEM 09",
        "name": "AvaliaMatch PRO",
        "category": "Avaliação Imobiliária",
        "keyword": "ia avaliacao de imoveis",
        "title": "AvaliaMatch PRO | IA para Avaliação de Imóveis (NBR 14653)",
        "meta_desc": "Elabore laudos de avaliação de imóveis urbanos pelo Método Comparativo Direto de Dados de Mercado em conformidade com a NBR 14653 com IA.",
        "short_desc": "Engenharia de avaliações: método comparativo direto, tratamento estatístico de dados de mercado, laudos bancários e perícias.",
        "gemini_link": "https://gemini.google.com/gem/1V6d6n_LtnrlgD847HtWmjmC-baKKIc3V?usp=sharing",
        "emoji": "🏠",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Laudos de Avaliação de Imóveis (NBR 14653) Prontos para Bancos e Perícias",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
            </svg>
        """,
        "problem_now": "A engenharia de avaliações de imóveis urbanos exige muito rigor estatístico. Pesquisar comparativos de mercado corretos, aplicar fatores de homogeneização de padrão, área, testada e localização manualmente, além de enquadrar o Grau de Precisão e Fundamentação da NBR 14653-2 toma dias inteiros de trabalho de planilhamento e abre espaço para descarte incorreto de comparativos e contestações periciais judiciais.",
        "transformation": "Com o AvaliaMatch PRO, você simplifica o tratamento estatístico. O agente ajuda a planejar a vistoria de mercado, estruturar a planilha de homogeneização por fatores (Fator de Área, Padrão Construtivo, Localização), orienta sobre a exclusão de outliers por critérios matemáticos (como o teste de Chauvenet) e auxilia no cálculo da depreciação pelo método Ross-Heidecke de edificações antigas.",
        "features": [
            {"title": "Método Comparativo de Mercado", "desc": "Estrutura avaliações com base na coleta de dados, fatores de homogeneização e regressões lineares conforme NBR 14653.", "benefit": "Tratamento de dados científicos e padronizados."},
            {"title": "Laudos de Garantia Bancária", "desc": "Agiliza a elaboração de laudos técnicos exigidos por bancos para financiamentos habitacionais e garantias reais.", "benefit": "Aprovação de processos de crédito ágeis e corretos."},
            {"title": "Métodos de Renda e Evolutivo", "desc": "Avaliação de aluguéis e taxas de capitalização (Método da Renda) ou cálculo de custo de reprodução de imóveis únicos (Método Evolutivo).", "benefit": "Versatilidade metodológica para qualquer tipo de imóvel."},
            {"title": "Tratamento Estatístico e Outliers", "desc": "Orienta no descarte de dados discrepantes da amostra utilizando o critério estatístico de Chauvenet.", "benefit": "Precisão matemática e consistência estatística."}
        ],
        "steps": [
            {"step": "1", "title": "Descreva o Imóvel Avaliando", "desc": "Forneça as características básicas do imóvel (área construída, idade, padrão, vagas de garagem e localização)."},
            {"step": "2", "title": "Amostra de Comparativos", "desc": "Insira os dados coletados de imóveis similares ofertados na mesma região (comparativos de mercado)."},
            {"step": "3", "title": "Homogeneização de Dados", "desc": "O AvaliaMatch PRO calcula e orienta sobre a aplicação dos fatores de correção e homogeneização estatística."},
            {"step": "4", "title": "Valor de Mercado Final", "desc": "Obtenha o valor de mercado estruturado, a faixa de preços admissível e as diretrizes para classificar o Grau de Fundamentação."}
        ],
        "prompts": [
            {
                "name": "Homogeneização por Fatores (NBR 14653-2)",
                "objective": "Estruturar o cálculo dos fatores de área e localização para dados de mercado.",
                "instruction": "Você é o AvaliaMatch PRO. Explique e monte o memorial de cálculo para homogeneizar uma amostra de comparativos em relação a um imóvel avaliando de [AREA_AVALIANDO] m². O comparativo 1 possui [AREA_COMP1] m² e fator de localização de [LOC_COMP1]. Aplique os fatores de área e de transposição de oferta recomendados pela NBR 14653-2.",
                "placeholders": "[AREA_AVALIANDO] (ex: 120), [AREA_COMP1] (ex: 150), [LOC_COMP1] (ex: 0.90)"
            },
            {
                "name": "Depreciação por Ross-Heidecke",
                "objective": "Calcular a depreciação física de uma benfeitoria antiga.",
                "instruction": "Você é o AvaliaMatch PRO. Calcule o coeficiente de depreciação física de Ross-Heidecke (kd) e o valor depreciado de uma edificação comercial que possui [IDADE_IMOVIL] anos de idade real, vida útil regulamentar estimada em [VIDA_UTIL] anos, com estado de conservação classificado como [ESTADO_CONSERVACAO] (conforme tabela de Ross-Heidecke). O custo de reprodução a novo estimado é de [CUSTO_NOVO].",
                "placeholders": "[IDADE_IMOVIL] (ex: 18), [VIDA_UTIL] (ex: 50), [ESTADO_CONSERVACAO] (ex: regular carecendo de reparos simples), [CUSTO_NOVO] (ex: R$ 450.000,00)"
            },
            {
                "name": "Metodologia de Avaliação pelo Método da Renda",
                "objective": "Estimar o valor do imóvel com base no rendimento de locação.",
                "instruction": "Você é o AvaliaMatch PRO. Estruture a memória de cálculo para estimar o valor de mercado de um imóvel comercial cujo aluguel mensal líquido projetado é de [ALUGUEL_MENSAL] por mês. Considere uma taxa de capitalização de mercado recomendada de [TAXA_CAP]% ao ano e período de projeção de [PRAZO] meses, indicando a fórmula e fundamentação teórica.",
                "placeholders": "[ALUGUEL_MENSAL] (ex: R$ 6.500,00), [TAXA_CAP] (ex: 7.5), [PRAZO] (ex: 120)"
            },
            {
                "name": "Enquadramento de Grau de Fundamentação",
                "objective": "Identificar os requisitos técnicos atendidos para classificar a fundamentação do laudo.",
                "instruction": "Você é o AvaliaMatch PRO. Elabore o checklist de verificação de requisitos mínimos exigidos pela NBR 14653-2 para classificar um laudo de avaliação de imóvel urbano com Grau [GRAU_ALVO] de Fundamentação, focando na identificação dos dados, identificação das variáveis e número de elementos da amostra.",
                "placeholders": "[GRAU_ALVO] (ex: II)"
            }
        ],
        "benefits": [
            "Conformidade Bancária: Estrutura técnica aceita por instituições financeiras (Caixa, BB, etc.) para garantia real.",
            "Rigor Estatístico: Eliminação de achismos no cálculo de fatores de padrão, localização e cubagem.",
            "Laudos Periciais Robustos: Pareceres de avaliação imobiliária que resistem a impugnações judiciais com facilidade."
        ],
        "for_whom": [
            "Engenheiros e Arquitetos Avaliadores: que elaboram laudos periciais judiciais ou laudos para contratação de garantias de crédito.",
            "Peritos de Engenharia e Corretores Avaliadores (CNAI): que desejam fundamentar estatisticamente seus valores de mercado.",
            "Escritórios Técnicos e Incorporadoras: que realizam pesquisas rápidas de terrenos e valores de venda de empreendimentos."
        ],
        "included": [
            "Acesso imediato ao agente AvaliaMatch PRO no Google Gemini.",
            "4 prompts de homogeneização, depreciação, método da renda e enquadramento.",
            "Guia prático em PDF de fatores de homogeneização da NBR 14653.",
            "Atualizações automáticas alinhadas à evolução de IA na engenharia."
        ],
        "faq": [
            {"q": "O AvaliaMatch PRO realiza cálculos de regressão linear sozinho?", "a": "O agente orienta sobre a montagem da planilha, tratamento dos dados, cálculo dos fatores (fator de área, localização) e interpretação estatística. Para rodar a estatística inferencial complexa, recomenda-se usar softwares de apoio (como SISDEA ou TS-Sisvel) sob a orientação técnica estruturada pelo agente."},
            {"q": "Ele é válido para avaliações periciais judiciais?", "a": "Sim. A metodologia empregada nas respostas do agente baseia-se estritamente na NBR 14653 (partes 1 e 2), fornecendo embasamento técnico que resiste a impugnações judiciais."},
            {"q": "O agente ajuda a identificar o Grau de Precisão do laudo?", "a": "Sim, auxiliando na conferência dos critérios normativos exigidos para enquadramento de Grau I, II ou III de Fundamentação e Precisão."},
            {"q": "Como funciona a homogeneização por fatores no agente?", "a": "Você insere os dados do imóvel de referência e dos comparativos, e o agente calcula as proporções analíticas básicas aplicando as fórmulas recomendadas pela metodologia científica de avaliações."},
            {"q": "O agente tem integração direta com portais imobiliários?", "a": "O agente pode realizar buscas na web em tempo real (via Google Search integrado no Gemini) para identificar imóveis semelhantes ofertados na região desejada, auxiliando na formação inicial da amostra."},
            {"q": "Ele calcula o Método Evolutivo e Involutivo?", "a": "Sim. O agente fornece a roteirização do cálculo de viabilidade econômica do empreendimento (Método Involutivo) e o somatório depreciado de benfeitorias + terreno (Método Evolutivo)."},
            {"q": "Corretores de imóveis com CNAI podem utilizar o agente?", "a": "Perfeitamente. O agente auxilia na redação técnica de PTAMs (Parecer Técnico de Avaliação Mercadológica) em conformidade com as exigências metodológicas."},
            {"q": "Onde recebo os acessos da suíte Agentes Match?", "a": "Os links de acesso e o guia técnico de prompts são disponibilizados de forma automática por e-mail e na área de membros de imediato após a aprovação do seu pagamento."}
        ]
    },
    {
        "filename": "mockups-arquitetura-renders-ia.html",
        "gem_number": "GEM 10",
        "name": "ArquiMatch PRO",
        "category": "Visualização e Conceito",
        "keyword": "ia maquete 3d arquitetura",
        "title": "ArquiMatch PRO | IA para Renders e Design de Interiores",
        "meta_desc": "Gere prompts fotorrealistas para maquetes 3D, renders de fachada e designs de interiores utilizando IA. Otimizado para Imagen 3 e Veo 3.1.",
        "short_desc": "Consultoria em visualização arquitetônica, prompts fotorrealistas de render, memoriais conceituais e tours virtuais imersivos.",
        "gemini_link": "https://gemini.google.com/gem/1V5h5K0Q4voH1Pi0H-7WsfOI28fIMvBfC?usp=sharing",
        "emoji": "🎨",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Gere Renders Fotorrealistas e Memorial Descritivo Conceitual com IA",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.53 16.122l.188-.465a.6.6 0 00-.07-.528l-.307-.356a.6.6 0 00-.77 0l-.307.356a.6.6 0 00-.071.528l.189.465m6.858 0l.189-.465a.6.6 0 00-.07-.528l-.307-.356a.6.6 0 00-.77 0l-.307.356a.6.6 0 00-.07.528l.189.465m0 0a8.25 8.25 0 11-10.744 0m10.744 0a8.25 8.25 0 10-10.744 0M12 3v13.5"/>
            </svg>
        """,
        "problem_now": "Apresentar ideias de projetos arquitetônicos e designs de interiores para clientes na fase de concepção inicial requer um tempo imenso de modelagem 3D e renderização em softwares como V-Ray ou Lumion. Muitas vezes, o cliente deseja testar diferentes paletas de cores, fachadas ou disposições de mobiliário, e re-renderizar essas opções manualmente atrasa o fechamento de novos contratos.",
        "transformation": "Com o ArquiMatch PRO, você revoluciona o seu processo criativo. O agente gera prompts extremamente detalhados de fotografia arquitetônica (regras de lentes, iluminação realista, texturas PBR, etc.) calibrados para ferramentas de geração de imagem de alta performance como o Imagen 3. Ele também auxilia na redação de memoriais conceituais elegantes e roteiros para vídeos dinâmicos de tours virtuais imersivos no Veo 3.1.",
        "features": [
            {"title": "Prompts Fotorrealistas de Render", "desc": "Cria comandos super-detalhados de fotografia arquitetônica (regras de lente, iluminação global, materiais PBR) para ferramentas de geração de imagem como Imagen 3.", "benefit": "Imagens conceituais ultra-realistas em segundos."},
            {"title": "Memoriais Conceituais de Elite", "desc": "Redige memoriais descritivos conceituais e narrativas de projeto que encantam clientes e defendem as escolhas de design.", "benefit": "Defesa de partido arquitetônico eloquente e profissional."},
            {"title": "Estudos de Insolação e Fachadas", "desc": "Gera prompts para simular a luz do sol nas fachadas em diferentes horários do dia, facilitando escolhas de brises e aberturas.", "benefit": "Simulações térmicas e visuais ágeis de iluminação."},
            {"title": "Roteiros para Vídeos (Veo 3.1)", "desc": "Roteiriza tours 360° e sequências construtivas animadas de curta duração para apresentar o espaço de forma dinâmica.", "benefit": "Apresentações em vídeo inovadoras para incorporações."}
        ],
        "steps": [
            {"step": "1", "title": "Defina o Partido Arquitetônico", "desc": "Forneça as diretrizes básicas do design (moderno, industrial, biofílico), materiais de acabamento e a iluminação alvo."},
            {"step": "2", "title": "Gere o Prompt de Render", "desc": "O ArquiMatch PRO estrutura um comando fotorrealista com linguagem de câmera (lente, ISO, luz) específica para IA."},
            {"step": "3", "title": "Renderização Instantânea", "desc": "Cole o prompt no Imagen 3 (ou ferramenta de imagem/vídeo) para obter o mockup visual instantaneamente."},
            {"step": "4", "title": "Apresentação ao Cliente", "desc": "Utilize os mockups visuais e a narrativa conceitual gerada pelo agente para fechar a aprovação preliminar do cliente."}
        ],
        "prompts": [
            {
                "name": "Prompt para Render de Fachada",
                "objective": "Gerar um prompt fotorrealista de arquitetura externa para o Imagen 3.",
                "instruction": "Você é o ArquiMatch PRO. Elabore um prompt em inglês técnico de alta precisão fotográfica para o Imagen 3 gerar uma fachada residencial de estilo [ESTILO], com acabamentos em [MATERIAIS]. A cena deve estar ambientada sob iluminação de [HORARIO] em um dia [CLIMA], utilizando câmera com lente de [LENTE] e foco focado no detalhe geométrico da entrada.",
                "placeholders": "[ESTILO] (ex: minimalista contemporâneo), [MATERIAIS] (ex: concreto aparente ripado, madeira cumaru e esquadrias pretas), [HORARIO] (ex: golden hour / entardecer), [CLIMA] (ex: ligeiramente úmido com reflexos na calçada), [LENTE] (ex: 24mm tilt-shift)"
            },
            {
                "name": "Prompt para Render de Interior",
                "objective": "Gerar um prompt fotorrealista de sala ou quarto para IA.",
                "instruction": "Você é o ArquiMatch PRO. Elabore um prompt técnico e artístico para renderizar uma sala de estar com pé-direito duplo integrada com cozinha gourmet. O estilo de design de interiores deve ser [ESTILO_INTERIOR], com destaque para a textura de [TEXTURA_DESTAQUE] e iluminação proveniente de [ILUMINACAO_FONTE].",
                "placeholders": "[ESTILO_INTERIOR] (ex: escandinavo moderno com toques brasileiros), [TEXTURA_DESTAQUE] (ex: sofá de linho cru, tapete de fibra natural e painel de freijó), [ILUMINACAO_FONTE] (ex: grandes aberturas de vidro com luz difusa de claraboia)"
            },
            {
                "name": "Memorial Conceitual (Copywriting)",
                "objective": "Escrever a narrativa conceitual e de partido para encantar o cliente.",
                "instruction": "Você é o ArquiMatch PRO. Escreva um memorial descritivo conceitual de apresentação para o projeto de uma [TIPO_PROJETO] com área de [AREA] m². O conceito de projeto é focado em [CONCEITO_FOCO] e integra soluções de sustentabilidade como [SUSTENTABILIDADE]. Adote um tom poético, elegante e técnico simultaneamente.",
                "placeholders": "[TIPO_PROJETO] (ex: residência unifamiliar serrana), [AREA] (ex: 280), [CONCEITO_FOCO] (ex: integração interna-externa e sensação de acolhimento), [SUSTENTABILIDADE] (ex: ventilação cruzada natural, aproveitamento de água de chuva e energia fotovoltaica)"
            },
            {
                "name": "Roteiro de Tour Virtual (Vídeo)",
                "objective": "Roteirizar cenas para geração de vídeo conceitual.",
                "instruction": "Você é o ArquiMatch PRO. Crie o roteiro detalhado de cenas (storyboard) para um vídeo conceitual de [DURACAO] segundos apresentando a transição do [CENA_ORIGEM] para a [CENA_DESTINO], ideal para gerar um clipe de animação no Google Veo 3.1, descrevendo movimentos de câmera lentos e cinematic.",
                "placeholders": "[DURACAO] (ex: 15), [CENA_ORIGEM] (ex: jardim de entrada da casa sob a luz da manhã), [CENA_DESTINO] (ex: área social interna com transição de cortinas movidas a vento suave)"
            }
        ],
        "benefits": [
            "Concepção Veloz: Simule 20 alternativas visuais de cores e materiais em minutos para o cliente escolher antes de iniciar o CAD/BIM.",
            "Textos de Encantamento: Redação de memoriais descritivos artísticos e justificativas de projeto eloquentes e persuasivas.",
            "Inovação Visual: Domine as ferramentas de vanguarda de geração de vídeo (Veo) e imagem (Imagen) do ecossistema Google."
        ],
        "for_whom": [
            "Arquitetos e Designers de Interiores: que desejam demonstrar conceitos estéticos rápidos aos clientes sem gastar horas de renderizador 3D.",
            "Paisagistas e Urbanistas: que necessitam simular inserções vegetais e mobiliários urbanos de forma fotorrealista.",
            "Incorporadoras e Setores de Vendas Imobiliárias: que precisam gerar mockups rápidos para campanhas de marketing."
        ],
        "included": [
            "Acesso imediato ao agente ArquiMatch PRO no Google Gemini.",
            "4 prompts fotorrealistas de renderização de arquitetura e redação de memoriais.",
            "Guia rápido digital com os principais códigos de iluminação e lentes para IA.",
            "Acesso a atualizações do agente conforme novos updates do Imagen e Veo."
        ],
        "faq": [
            {"q": "O ArquiMatch PRO gera modelos 3D editáveis (BIM/CAD)?", "a": "Não. O agente cria mockups conceituais de imagem/vídeo e orientações de visualização e design, servindo para aprovação de conceito rápido. A modelagem 3D técnica continua exigindo softwares como Revit, SketchUp ou Archicad."},
            {"q": "Como funciona a geração de vídeo com o Veo 3.1?", "a": "O agente ajuda a estruturar a narrativa técnica e a descrever a trajetória da câmera, os elementos em movimento e a luz para que você use na ferramenta de geração de vídeos (Veo) do ecossistema Google."},
            {"q": "Posso usar os memoriais gerados para fins comerciais?", "a": "Sim, os memoriais descritivos e textos conceituais são de sua propriedade intelectual e podem ser usados comercialmente para apresentação de projetos a clientes."},
            {"q": "Quais são os prompts mais eficientes para renders internos?", "a": "O agente fornece prompts com tags específicas como iluminação volumétrica, materiais PBR (wood grain, brushed steel), especificações de lente (35mm f/1.8) e estilo de composição visual."},
            {"q": "É necessário ter uma licença premium do Imagen 3?", "a": "Não. O Imagen 3 e o Gemini estão disponíveis gratuitamente nas plataformas oficiais do Google, embora as versões pagas possam oferecer processamento acelerado."},
            {"q": "Consigo simular reformas (retrofit) com fotos existentes?", "a": "Sim. Na versão multimodal do Gemini, você carrega a foto do imóvel existente e utiliza o prompt do ArquiMatch PRO especificando quais elementos manter e quais reformar."},
            {"q": "O agente ajuda a definir a paleta de cores do projeto?", "a": "Com certeza. Ele sugere paletas de cores de acordo com teorias de psicologia ambiental, estilo arquitetônico e as tendências de design de interiores vigentes."},
            {"q": "Quantas imagens posso gerar por dia?", "a": "A geração de imagem é feita na plataforma do Gemini, sujeita aos limites de uso diário definidos pelas políticas de uso do ecossistema do Google."}
        ]
    },
    {
        "filename": "marketing-conseguir-clientes-ia.html",
        "gem_number": "GEM 02",
        "name": "PubliMatch PRO",
        "category": "Marketing e Vendas",
        "keyword": "marketing para engenheiros ia",
        "title": "PubliMatch PRO | IA para Marketing e Clientes na Engenharia",
        "meta_desc": "Descubra estratégias de marketing digital para engenheiros, copywriting para postagens de obras no Instagram e prospecção de clientes com IA.",
        "short_desc": "Marketing digital ético e estratégico (CREA/CONFEA), scripts de WhatsApp, SEO local e copy de alta conversão para engenheiros.",
        "gemini_link": "https://gemini.google.com/gem/1seZSo0D2p9CIE6T4S2QY__9xwVqhZnEE?usp=sharing",
        "emoji": "📢",
        "color": "#D4AF37",
        "checkout_link": "https://pay.cakto.com.br/3dzpj4v",
        "headline": "Atraia Clientes Qualificados de Engenharia e Domine o SEO Local",
        "icon_svg": """
            <svg class="w-8 h-8 text-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M10.34 15.84c-.68.34-1.34.08-1.34-.62V8.78c0-.7.66-.96 1.34-.62l5.22 2.61c.68.34.68.9 0 1.24l-5.22 2.61zM21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
        """,
        "problem_now": "Conseguir novos clientes e fechar contratos de engenharia de alto valor (como obras de reforma ou projetos estruturais) é o maior desafio do profissional autônomo. Fazer postagens sem relevância no Instagram que não atraem leads qualificados, não saber prospectar síndicos e incorporadores por canais como WhatsApp, ou estar invisível no Google Maps local faz seu escritório ficar à mercê de indicações esporádicas.",
        "transformation": "Com o PubliMatch PRO, você constrói uma máquina de atração de clientes. O agente cria planejamentos editoriais de conteúdo altamente técnicos que demonstram sua autoridade sem ferir a ética do CREA/CONFEA. Ele redige scripts de abordagem pelo WhatsApp, otimiza seu perfil no Google Meu Negócio para buscas locais e cria propostas comerciais com gatilhos de conversão que aumentam a taxa de fechamento.",
        "features": [
            {"title": "Copywriting Técnico e Ético", "desc": "Cria roteiros, artigos e legendas altamente persuasivas respeitando as regras éticas de propaganda do CREA/CONFEA.", "benefit": "Divulgação de alto impacto sem risco de infrações éticas."},
            {"title": "Otimização de SEO Local", "desc": "Estratégias completas para posicionar seu escritório de engenharia no topo das buscas no Google Maps e Google Meu Negócio.", "benefit": "Clientes locais ligando e solicitando orçamentos diariamente."},
            {"title": "Scripts de WhatsApp e Prospecção", "desc": "Scripts de cold approach e prospecção de clientes particulares e corporativos para venda de serviços técnicos de valor elevado.", "benefit": "Abordagens comerciais seguras e profissionais."},
            {"title": "Planejamento Editorial Temático", "desc": "Cria cronogramas editoriais mensais baseados no seu nicho de atuação para atrair leads de forma qualificada.", "benefit": "Presença digital consistente e estratégica sem esforço."}
        ],
        "steps": [
            {"step": "1", "title": "Escolha o Canal e Público", "desc": "Defina o canal de marketing (Instagram, LinkedIn, Google Meu Negócio ou WhatsApp) e o seu cliente ideal (síndico, proprietário, construtora)."},
            {"step": "2", "title": "Gere a Estratégia de Copy", "desc": "O PubliMatch PRO formula a abordagem de conteúdo, as headlines magnéticas e a estruturação de dor e solução técnica."},
            {"step": "3", "title": "Aplique nos Canais", "desc": "Copie e programe as postagens nas suas mídias sociais ou envie as mensagens de abordagem comercial direta."},
            {"step": "4", "title": "Conversão e Contrato", "desc": "Converta os contatos recebidos em reuniões qualificadas e utilize os scripts de fechamento e propostas comerciais geradas pelo agente."}
        ],
        "prompts": [
            {
                "name": "Script de WhatsApp para Síndicos",
                "objective": "Prospectar síndicos para vender serviços de laudo de inspeção predial.",
                "instruction": "Você é o PubliMatch PRO. Crie um script de abordagem fria (cold message) em tom extremamente profissional para o WhatsApp, direcionado a síndicos de condomínios da minha cidade, propondo uma reunião rápida para apresentar meu serviço de [SERVICO_PROSPECCAO]. Evite termos excessivamente informais e foque na prevenção de multas e acidentes.",
                "placeholders": "[SERVICO_PROSPECCAO] (ex: laudo de vistoria técnica e inspeção predial obrigatória da Lei Municipal)"
            },
            {
                "name": "Otimização Google Meu Negócio (SEO)",
                "objective": "Posicionar o perfil do escritório no topo do Google Maps.",
                "instruction": "Você é o PubliMatch PRO. Elabore a descrição otimizada para SEO local e a lista das 15 palavras-chave mais estratégicas para preencher no Google Meu Negócio de um escritório de engenharia civil especializado em [ESPECIALIDADE] localizado na cidade de [CIDADE].",
                "placeholders": "[ESPECIALIDADE] (ex: cálculo estrutural de concreto e fundações), [CIDADE] (ex: Campinas - SP)"
            },
            {
                "name": "Carrossel Educativo para Instagram",
                "objective": "Gerar roteiro de slides de alta conversão para atrair leads particulares.",
                "instruction": "Você é o PubliMatch PRO. Roteirize um carrossel de [SLIDES] slides para o Instagram explicando de forma didática o tema [TEMA_CARROSSEL]. O objetivo é educar o cliente final leigo e conscientizar sobre a necessidade de contratar um engenheiro civil. Inclua a copy exata de cada slide e uma chamada para ação (CTA) final.",
                "placeholders": "[SLIDES] (ex: 6), [TEMA_CARROSSEL] (ex: 5 sinais silenciosos de que a infiltração está comprometendo a estrutura da sua casa)"
            },
            {
                "name": "Artigo de Autoridade para LinkedIn",
                "objective": "Redigir artigo corporativo voltado para parcerias com construtoras.",
                "instruction": "Você é o PubliMatch PRO. Escreva um artigo robusto para o LinkedIn focado em demonstrar a importância estratégica do [SERVICO_B2B] para construtoras e incorporadoras que visam reduzir prazos e custos na fase de obras. Adote um tom de especialista corporativo (B2B).",
                "placeholders": "[SERVICO_B2B] (ex: compatibilização de projetos em BIM e coordenação técnica de engenharia)"
            }
        ],
        "benefits": [
            "Prospecção Ativa: Scripts e e-mails estruturados para contatar clientes corporativos sem parecer invasivo.",
            "Autoridade Incontestável: Conteúdos de engenharia com embasamento técnico e ético que atraem leads de alto valor.",
            "SEO Local Estruturado: Posicionamento no Google Maps que atrai clientes locais prontos para fechar contrato."
        ],
        "for_whom": [
            "Engenheiros Autônomos: que necessitam prospectar clientes de forma constante para sustentar o próprio escritório.",
            "Pequenos Escritórios Técnicos de Engenharia: que desejam iniciar sua estruturação de marketing digital e presença no Google.",
            "Profissionais de Consultoria e Perícia: que buscam contatar síndicos e administradoras de condomínio de forma profissional."
        ],
        "included": [
            "Acesso imediato ao agente PubliMatch PRO no Google Gemini.",
            "4 prompts de marketing estratégico para WhatsApp, Instagram, LinkedIn e SEO local.",
            "Guia de bolso de marketing ético para engenheiros de acordo com o CREA.",
            "Atualizações e dicas periódicas integradas de copy de vendas e atração de leads."
        ],
        "faq": [
            {"q": "As estratégias geradas respeitam o código de ética do CREA?", "a": "Sim, todas as abordagens comerciais, copys e roteiros são planejados para valorizar o conhecimento do engenheiro sem infringir os limites de ética profissional definidos pelo CONFEA."},
            {"q": "O PubliMatch PRO cria imagens prontas para posts?", "a": "O agente auxilia na redação, nos roteiros e na descrição detalhada de imagens que você pode gerar utilizando o Imagen 3 ou criar em ferramentas como o Canva."},
            {"q": "Ele serve para quem atua em nichos muito específicos de engenharia?", "a": "Sim. Você pode definir seu nicho exato (saneamento, terraplenagem, pontes, patologia) e o agente calibrará a linguagem técnica para atrair o público ideal."},
            {"q": "Consigo prospectar construtoras para vender projetos terceirizados?", "a": "Perfeitamente. O agente ajuda a escrever propostas comerciais de valor e e-mails de abordagem focados nos problemas de construtoras (atrasos, custos) para oferecer serviços de cálculo ou compatibilização."},
            {"q": "O Google Meu Negócio realmente atrai clientes sem anúncios pagos?", "a": "Sim. O SEO local estruturado posiciona seu perfil no topo das buscas geolocalizadas orgânicas da sua região quando as pessoas digitam 'engenheiro civil' ou 'laudo técnico', gerando contatos qualificados."},
            {"q": "Ele gera ideias de conteúdo para o ano todo?", "a": "O agente pode estruturar calendários editoriais de 30 dias de forma recorrente, variando os temas de posts de atração, conexão e venda direta de acordo com seu portfólio."},
            {"q": "Como utilizar os scripts de WhatsApp?", "a": "Basta copiar a mensagem elaborada pelo agente, adaptar os campos entre colchetes com os seus dados de contato e do cliente, e iniciar o contato pelo WhatsApp de forma humana e profissional."},
            {"q": "Quais são as formas de pagamento para ter acesso à suíte?", "a": "O pagamento é efetuado através da plataforma segura da Cakto via Pix ou cartão de crédito em até 12 parcelas, com liberação de acesso imediata."}
        ]
    }
]

# Shared HTML Template (using {{variable}} for python replacements)
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
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            gold: '#D4AF37',
            goldLight: '#F4E4A0',
            goldDark: '#A68B2A',
            carbon: '#050505',
            carbonLight: '#111111',
            carbonMid: '#1a1a1a',
            carbonHover: '#222222',
          },
          fontFamily: {
            display: ['Playfair Display', 'serif'],
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
          animation: {
            'blob': 'blob 7s infinite',
            'float': 'float 4s ease-in-out infinite',
          },
          keyframes: {
            blob: {
              '0%': { transform: 'translate(0px, 0px) scale(1)' },
              '33%': { transform: 'translate(30px, -50px) scale(1.1)' },
              '66%': { transform: 'translate(-20px, 20px) scale(0.9)' },
              '100%': { transform: 'translate(0px, 0px) scale(1)' },
            },
            float: {
              '0%, 100%': { transform: 'translateY(0)' },
              '50%': { transform: 'translateY(-10px)' },
            }
          }
        }
      }
    }
  </script>

  <style>
    body {
      background-color: #050505;
      color: #e5e5e5;
      overflow-x: hidden;
    }

    ::selection {
      background: #D4AF37;
      color: #050505;
    }

    .glass-card {
      background: rgba(26, 26, 26, 0.4);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(212, 175, 55, 0.15);
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
      transition: all 0.4s ease;
    }

    .glass-card:hover {
      border-color: rgba(212, 175, 55, 0.4);
      background: rgba(30, 30, 30, 0.6);
      transform: translateY(-4px);
      box-shadow: 0 12px 40px 0 rgba(212, 175, 55, 0.1);
    }

    .form-input {
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #fff;
      transition: all 0.3s ease;
    }

    .form-input:focus {
      outline: none;
      border-color: #D4AF37;
      box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
      background: rgba(0, 0, 0, 0.8);
    }

    .btn-premium {
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
    }

    .btn-premium:hover {
      background-position: right center;
      box-shadow: 0 6px 25px rgba(212, 175, 55, 0.5);
      transform: translateY(-2px);
    }

    .btn-premium:active {
      transform: translateY(1px);
    }

    .btn-outline {
      background: transparent;
      border: 1px solid rgba(212, 175, 55, 0.4);
      color: #D4AF37;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      transition: all 0.3s ease;
    }

    .btn-outline:hover {
      background: rgba(212, 175, 55, 0.1);
      border-color: #D4AF37;
    }

    .text-gradient-gold {
      background: linear-gradient(135deg, #e8c872 0%, #D4AF37 50%, #b38b1d 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .gold-grid-bg {
      background-image:
        linear-gradient(to right, rgba(212, 175, 55, 0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(212, 175, 55, 0.05) 1px, transparent 1px);
      background-size: 40px 40px;
    }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #050505; }
    ::-webkit-scrollbar-thumb { background: #2A2A2A; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #D4AF37; }

    details > summary { list-style: none; cursor: pointer; }
    details > summary::-webkit-details-marker { display: none; }
    details[open] .faq-icon { transform: rotate(45deg); }

    .reveal {
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .reveal.active { opacity: 1; transform: translateY(0); }

    .copy-btn {
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .copy-btn:hover {
      background: rgba(212, 175, 55, 0.15);
      border-color: #D4AF37;
    }

    a:focus-visible, button:focus-visible, input:focus-visible, summary:focus-visible {
      outline: 2px solid #D4AF37;
      outline-offset: 2px;
      border-radius: 4px;
    }
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { animation: none !important; transition: none !important; }
      .reveal { opacity: 1; transform: none; }
      html { scroll-behavior: auto; }
    }
  </style>

  <!-- Structured Data (JSON-LD) SoftwareApplication -->
  {{software_app_json_ld}}

  <!-- Structured Data (JSON-LD) FAQ -->
  {{faq_json_ld}}
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
        <a href="#como-funciona" class="text-gray-400 hover:text-white transition-colors">Como funciona</a>
        <a href="#recursos" class="text-gray-400 hover:text-white transition-colors">Recursos</a>
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
            <span class="font-mono text-[11px] text-white font-bold uppercase tracking-widest">{{gem_number}} · {{category}}</span>
          </div>

          <h1 class="font-display text-4xl sm:text-5xl lg:text-6xl font-bold leading-[1.08] tracking-tight mb-6 text-white">
            {{headline}}
          </h1>

          <p class="text-lg lg:text-xl text-gray-400 mb-8 max-w-2xl leading-relaxed font-light font-sans">
            {{short_desc}} Tenha um copiloto de inteligência artificial de alta performance integrado ao seu Google Gemini.
          </p>

          <div class="flex gap-4 mb-8">
            <a href="#inicio" class="btn-premium px-6 py-3.5 rounded-lg text-xs font-bold uppercase tracking-wider">
              Abrir Agente no Gemini ↗
            </a>
            <a href="#prompts" class="btn-outline px-6 py-3.5 rounded-lg text-xs font-bold uppercase tracking-wider">
              Visualizar Prompts
            </a>
          </div>
        </div>

        <!-- Right: Lead Form Box / Chat Simulation -->
        <div class="lg:col-span-5 reveal relative">
          <div class="absolute -inset-1 bg-gradient-to-r from-gold/20 to-transparent rounded-2xl blur-lg opacity-40"></div>
          <div class="glass-card rounded-2xl p-6 lg:p-8 relative z-10 border border-white/10">
            <div id="leadFormContainer">
              <h3 class="text-lg font-bold text-white mb-2">Libere o acesso ao {{name}} no Gemini</h3>
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
              <p class="text-xs text-gray-400 mb-6">Abrimos o agente {{name}} no seu Gemini em uma nova janela.</p>
              <a href="{{gemini_link}}" target="_blank" rel="noopener" class="btn-premium px-8 py-3 rounded text-xs inline-block">Abrir no Gemini</a>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- PROBLEM & TRANSFORMATION -->
    <section class="py-24 bg-carbon border-t border-white/5" id="problema-transformacao">
      <div class="max-w-6xl mx-auto px-6 reveal">
        <div class="grid lg:grid-cols-12 gap-12 items-center">
          <div class="lg:col-span-6 space-y-6">
            <div class="w-10 h-10 bg-red-500/10 rounded-full flex items-center justify-center text-red-500 font-bold border border-red-500/20">✕</div>
            <span class="font-mono text-red-400 text-xs uppercase tracking-widest font-bold block">O Cenário Manual e Ineficiente</span>
            <h2 class="font-display text-3xl lg:text-4xl font-bold text-white leading-tight">Como a tarefa é realizada hoje</h2>
            <p class="text-gray-400 leading-relaxed font-light text-sm">
              {{problem_now}}
            </p>
          </div>
          <div class="lg:col-span-6 space-y-6 bg-gold/5 border border-gold/15 p-8 lg:p-10 rounded-3xl">
            <div class="w-10 h-10 bg-gold/10 rounded-full flex items-center justify-center text-gold font-bold border border-gold/20">✔</div>
            <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold block">A Solução Inteligente</span>
            <h2 class="font-display text-3xl lg:text-4xl font-bold text-white leading-tight">A Transformação Prática</h2>
            <p class="text-gray-300 leading-relaxed font-light text-sm">
              {{transformation}}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURES -->
    <section class="py-24 bg-carbonLight/50 border-t border-white/5" id="recursos">
      <div class="max-w-6xl mx-auto px-6">
        <div class="text-center mb-16 reveal">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Recursos e Funcionalidades</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 mb-4 text-white">Como o {{name}} funciona na prática</h2>
          <p class="text-gray-400 max-w-2xl mx-auto">Desenvolvido por especialistas da construção, integrando conhecimentos reais a fluxos ágeis de IA.</p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 reveal">
          {{features_cards}}
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS -->
    <section class="py-24 bg-carbon border-t border-white/5" id="como-funciona">
      <div class="max-w-6xl mx-auto px-6 reveal">
        <div class="text-center mb-16">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Fluxo de Trabalho</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 text-white">Como Utilizar em 4 Passos</h2>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {{how_it_works_steps}}
        </div>
      </div>
    </section>

    <!-- PROMPTS SWIPE FILE -->
    <section class="py-24 bg-carbonLight/50 border-t border-white/5 relative" id="prompts">
      <div class="max-w-5xl mx-auto px-6 reveal">
        <div class="text-center mb-16">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Acervo de Prompts</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 mb-4 text-white">Copie e use no seu Gemini</h2>
          <p class="text-gray-400">Modelos de comando altamente precisos estruturados para extrair os melhores resultados técnicos.</p>
        </div>

        <div class="grid md:grid-cols-2 gap-8">
          {{prompts_cards}}
        </div>
      </div>
    </section>

    <!-- BENEFITS -->
    <section class="py-24 bg-carbon border-t border-white/5" id="beneficios">
      <div class="max-w-6xl mx-auto px-6 reveal">
        <div class="text-center mb-16">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Vantagens Reais</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 text-white">Por que integrar o {{name}} ao seu fluxo</h2>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
          {{benefits_cards}}
        </div>
      </div>
    </section>

    <!-- FOR WHOM -->
    <section class="py-24 bg-carbonLight/50 border-t border-white/5" id="para-quem">
      <div class="max-w-5xl mx-auto px-6 reveal">
        <div class="text-center mb-16">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Público-Alvo</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 text-white">Para quem é recomendado?</h2>
        </div>
        <div class="grid sm:grid-cols-2 md:grid-cols-3 gap-6">
          {{for_whom_elements}}
        </div>
      </div>
    </section>

    <!-- WHAT IS INCLUDED -->
    <section class="py-24 bg-carbon border-t border-white/5" id="o-que-esta-incluido">
      <div class="max-w-4xl mx-auto px-6 reveal">
        <div class="glass-card rounded-3xl p-8 lg:p-12 border border-gold/20 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-64 h-64 bg-gold/5 rounded-full filter blur-[50px] -z-10"></div>
          <div class="text-center mb-8">
            <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Acesso Completo</span>
            <h2 class="font-display text-3xl lg:text-4xl font-bold text-white mt-2">O que você recebe ao adquirir?</h2>
          </div>
          <ul class="space-y-4 text-gray-300 text-sm max-w-2xl mx-auto mb-10">
            {{included_elements}}
          </ul>
          <div class="text-center">
            <p class="text-xs text-gray-500 mb-6">Adquira agora a suíte completa com 9 agentes de IA por preço promocional e impulsione seus resultados de engenharia civil.</p>
            <a href="{{checkout_link}}" target="_blank" rel="noopener" class="btn-premium px-8 py-4 rounded-lg text-sm text-center inline-block">Adquirir Acesso Completo (9 Agentes)</a>
          </div>
        </div>
      </div>
    </section>

    <!-- MONETIZATION / CTA -->
    <section class="py-24 bg-carbonLight border-t border-white/5 relative">
      <div class="absolute inset-0 bg-gold/5 pointer-events-none"></div>
      <div class="max-w-4xl mx-auto px-6 text-center reveal relative z-10">
        <h2 class="font-display text-4xl lg:text-5xl font-bold text-white mb-6">Eleve o nível do seu escritório técnico</h2>
        <p class="text-gray-400 mb-8 max-w-2xl mx-auto">O {{name}} faz parte da suíte premium de 9 agentes do Agentes Match. Garanta o acesso a todos os agentes e economize mais de 50%!</p>
        
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <a href="{{checkout_link}}" target="_blank" rel="noopener" class="btn-premium px-8 py-4 rounded-lg text-sm text-center">Adquirir Pacote Completo (9 Agentes)</a>
          <a href="#inicio" class="btn-outline px-8 py-4 rounded-lg text-sm text-center">Testar Este Agente Grátis</a>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="py-24 bg-carbon border-t border-white/5" id="faq">
      <div class="max-w-4xl mx-auto px-6">
        <div class="text-center mb-16 reveal">
          <span class="font-mono text-gold text-xs uppercase tracking-widest font-bold">Perguntas Frequentes</span>
          <h2 class="font-display text-3xl lg:text-5xl font-bold mt-3 mb-4 text-white">Dúvidas comuns sobre o {{name}}</h2>
        </div>

        <div class="space-y-4 reveal">
          {{faq_elements}}
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
            <li><a href="calculo-estrutural-dimensionamento-ia.html" class="hover:text-gold transition-colors">EstruturaMatch PRO (Cálculo)</a></li>
            <li><a href="avaliacao-imoveis-imobiliaria-ia.html" class="hover:text-gold transition-colors">AvaliaMatch PRO (Avaliações)</a></li>
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

      <div class="py-8 border-b border-white/5 text-[11px] text-gray-500 leading-relaxed max-w-4xl font-light">
        <p class="font-medium text-gray-400 mb-1">Aviso de Responsabilidade Técnica e Regulamentação:</p>
        <p>Os conteúdos gerados pela inteligência artificial devem ser revisados por um profissional qualificado antes de sua aplicação em projetos, obras, documentos técnicos ou decisões regulatórias. A utilização das sugestões fornecidas pelos agentes de inteligência artificial não exime o profissional habilitado (Engenheiro, Arquiteto, Orçamentista, etc.) da emissão da devida Anotação de Responsabilidade Técnica (ART) ou Registro de Responsabilidade Técnica (RRT) perante os órgãos de classe competentes (CREA / CAU).</p>
      </div>

      <div class="flex flex-col md:flex-row justify-between items-center gap-6 pt-8 text-xs text-gray-500 font-mono">
        <p>© 2026 ObraMatch. Todos os direitos reservados.</p>
        <div class="flex gap-6">
          <a href="#" class="hover:text-white transition-colors">Política de Privacidade</a>
          <a href="#" class="hover:text-white transition-colors">Termos de Uso</a>
          <a href="https://obramatch.com.br" target="_blank" rel="noopener" class="hover:text-white transition-colors">obramatch.com.br</a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    // Reveal Animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Form logic simulating Lead integration and redirecting
    const form = document.getElementById('agentForm');
    const leadFormContainer = document.getElementById('leadFormContainer');
    const successContainer = document.getElementById('successContainer');

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const whatsapp = document.getElementById('whatsapp').value;
      
      // Simulate API saving
      leadFormContainer.classList.add('hidden');
      successContainer.classList.remove('hidden');
      
      // Open Gemini link in a new window/tab
      window.open("{{gemini_link}}", "_blank");
    });

    // Header Dynamic Blur
    window.addEventListener('scroll', () => {
      const header = document.getElementById('header');
      if (window.scrollY > 20) {
        header.classList.add('bg-carbon/90', 'shadow-lg');
        header.classList.remove('bg-carbon/80');
      } else {
        header.classList.add('bg-carbon/80');
        header.classList.remove('bg-carbon/90', 'shadow-lg');
      }
    });

    // Prompts Copy function
    function copyPrompt(btn, id) {
      const textEl = document.getElementById(id);
      navigator.clipboard.writeText(textEl.innerText).then(() => {
        const originalText = btn.innerText;
        btn.innerText = 'COPIADO!';
        btn.classList.add('text-green-400', 'border-green-400');
        setTimeout(() => {
          btn.innerText = originalText;
          btn.classList.remove('text-green-400', 'border-green-400');
        }, 2000);
      });
    }
  </script>
</body>

</html>
"""

# Helper function to generate features cards
def make_features_cards(features, icon_svg):
    cards_html = ""
    for f in features:
        cards_html += f"""
          <div class="glass-card rounded-2xl p-6 lg:p-8">
            <div class="w-12 h-12 bg-gold/10 rounded-xl flex items-center justify-center mb-6 border border-gold/20">
              {icon_svg}
            </div>
            <h3 class="font-display text-xl font-bold text-white mb-3">{f['title']}</h3>
            <p class="text-sm text-gray-400 leading-relaxed font-light mb-4">{f['desc']}</p>
            <div class="text-[11px] text-gold font-semibold uppercase tracking-wider">⚡ Benefício Prático: {f['benefit']}</div>
          </div>
        """
    return cards_html

# Helper function to generate how it works steps
def make_how_it_works_steps(steps):
    steps_html = ""
    for s in steps:
        steps_html += f"""
          <div class="glass-card rounded-2xl p-6 border border-white/5 relative flex flex-col justify-between">
            <div>
              <div class="w-10 h-10 bg-gold/10 rounded-full flex items-center justify-center font-mono text-gold font-bold text-sm mb-6 border border-gold/20">
                {s['step']}
              </div>
              <h3 class="font-display text-lg font-bold text-white mb-3">{s['title']}</h3>
              <p class="text-xs text-gray-400 leading-relaxed font-light">{s['desc']}</p>
            </div>
          </div>
        """
    return steps_html

# Helper function to generate prompts cards
def make_prompts_cards(prompts, prefix_id):
    cards_html = ""
    for i, p in enumerate(prompts):
        id_str = f"prompt_{prefix_id}_{i}"
        cards_html += f"""
          <div class="glass-card rounded-2xl p-6 lg:p-8 border border-white/10 group flex flex-col justify-between">
            <div>
              <div class="flex justify-between items-center mb-4 pb-4 border-b border-white/5">
                <div class="flex items-center gap-3">
                  <span class="w-2.5 h-2.5 rounded-full bg-gold"></span>
                  <h4 class="font-display font-bold text-white text-base">Prompt {i+1} — {p['name']}</h4>
                </div>
                <button onclick="copyPrompt(this, '{id_str}')" class="copy-btn text-[10px] font-mono text-gold border border-gold/30 px-3 py-1.5 rounded hover:bg-gold hover:text-carbon transition-colors">
                  📋 Copiar Prompt
                </button>
              </div>
              <div class="mb-4">
                <span class="block text-[10px] font-mono uppercase tracking-wider text-gray-500 mb-1">Objetivo:</span>
                <p class="text-xs text-gray-300 font-light leading-relaxed">{p['objective']}</p>
              </div>
              <div class="mb-4">
                <span class="block text-[10px] font-mono uppercase tracking-wider text-gray-500 mb-1">Instrução (Pronta para usar):</span>
                <div class="bg-carbon/60 border border-white/5 rounded-lg p-4 font-mono text-xs text-gray-300 leading-relaxed select-all" id="{id_str}">{p['instruction']}</div>
              </div>
            </div>
            <div class="mt-4 pt-4 border-t border-white/5">
              <span class="block text-[10px] font-mono uppercase tracking-wider text-gold/70 mb-1">Campos para substituir:</span>
              <span class="text-xs text-gray-400 font-light italic">{p['placeholders']}</span>
            </div>
          </div>
        """
    return cards_html

# Helper function to generate benefits cards
def make_benefits_cards(benefits):
    cards_html = ""
    for b in benefits:
        parts = b.split(": ", 1)
        title = parts[0] if len(parts) > 1 else "Destaque"
        desc = parts[1] if len(parts) > 1 else b
        cards_html += f"""
          <div class="glass-card rounded-2xl p-6 lg:p-8 border border-white/5">
            <div class="text-gold text-2xl mb-4">✔</div>
            <h3 class="font-display text-lg font-bold text-white mb-2">{title}</h3>
            <p class="text-xs text-gray-400 leading-relaxed font-light">{desc}</p>
          </div>
        """
    return cards_html

# Helper function to generate for whom elements
def make_for_whom_elements(for_whom):
    elements_html = ""
    for w in for_whom:
        parts = w.split(": ", 1)
        title = parts[0] if len(parts) > 1 else "Profissional"
        desc = parts[1] if len(parts) > 1 else w
        elements_html += f"""
          <div class="glass-card rounded-2xl p-6 border border-white/5 flex gap-4 items-start">
            <div class="w-8 h-8 bg-gold/10 rounded-full flex items-center justify-center text-gold font-bold text-sm shrink-0 border border-gold/20">👤</div>
            <div>
              <h4 class="font-display font-semibold text-white text-sm mb-1">{title}</h4>
              <p class="text-xs text-gray-400 font-light leading-relaxed">{desc}</p>
            </div>
          </div>
        """
    return elements_html

# Helper function to generate included elements
def make_included_elements(included):
    elements_html = ""
    for item in included:
        elements_html += f"""
          <li class="flex items-center gap-3">
            <svg class="w-5 h-5 text-gold shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <span>{item}</span>
          </li>
        """
    return elements_html

# Helper function to generate FAQ elements
def make_faq_elements(faq):
    faq_html = ""
    for i, item in enumerate(faq):
        open_str = 'open' if i == 0 else ''
        faq_html += f"""
          <details class="glass-card rounded-xl p-5 border border-white/10" {open_str}>
            <summary class="flex justify-between items-center font-display font-semibold text-white">
              <span>{item['q']}</span>
              <span class="faq-icon text-gold transition-transform duration-300 font-mono text-xl">+</span>
            </summary>
            <div class="mt-4 text-sm text-gray-400 leading-relaxed font-light border-t border-white/5 pt-4">
              {item['a']}
            </div>
          </details>
        """
    return faq_html

# Generate the pages
for agent in agents_data:
    features_cards = make_features_cards(agent["features"], agent["icon_svg"])
    how_it_works_steps = make_how_it_works_steps(agent["steps"])
    prefix_id = agent["name"].lower().replace(" ", "").replace("ç", "c").replace("á", "a").replace("ó", "o")
    prompts_cards = make_prompts_cards(agent["prompts"], prefix_id)
    benefits_cards = make_benefits_cards(agent["benefits"])
    for_whom_elements = make_for_whom_elements(agent["for_whom"])
    included_elements = make_included_elements(agent["included"])
    faq_elements = make_faq_elements(agent["faq"])
    
    # Generate JSON-LD dynamically to avoid curly braces escaping issues
    app_json_ld_dict = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": agent["name"],
        "operatingSystem": "All",
        "applicationCategory": "BusinessApplication",
        "description": agent["meta_desc"],
        "offers": {
            "@type": "Offer",
            "price": "47.00",
            "priceCurrency": "BRL"
        }
    }
    software_app_json_ld = f'<script type="application/ld+json">\n{json.dumps(app_json_ld_dict, ensure_ascii=False, indent=2)}\n</script>'
    
    faq_entities = []
    for item in agent["faq"]:
        faq_entities.append({
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        })
    faq_json_ld_dict = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_entities
    }
    faq_json_ld = f'<script type="application/ld+json">\n{json.dumps(faq_json_ld_dict, ensure_ascii=False, indent=2)}\n</script>'

    # Format the final HTML using simple replacement of the placeholders
    file_content = html_template
    file_content = file_content.replace("{{title}}", agent["title"])
    file_content = file_content.replace("{{meta_desc}}", agent["meta_desc"])
    file_content = file_content.replace("{{name}}", agent["name"])
    file_content = file_content.replace("{{gem_number}}", agent["gem_number"])
    file_content = file_content.replace("{{keyword}}", agent["keyword"])
    file_content = file_content.replace("{{short_desc}}", agent["short_desc"])
    file_content = file_content.replace("{{gemini_link}}", agent["gemini_link"])
    file_content = file_content.replace("{{icon_svg}}", agent["icon_svg"])
    file_content = file_content.replace("{{checkout_link}}", agent["checkout_link"])
    file_content = file_content.replace("{{category}}", agent["category"])
    file_content = file_content.replace("{{headline}}", agent["headline"])
    file_content = file_content.replace("{{problem_now}}", agent["problem_now"])
    file_content = file_content.replace("{{transformation}}", agent["transformation"])
    
    # Injected HTML blocks
    file_content = file_content.replace("{{features_cards}}", features_cards)
    file_content = file_content.replace("{{how_it_works_steps}}", how_it_works_steps)
    file_content = file_content.replace("{{prompts_cards}}", prompts_cards)
    file_content = file_content.replace("{{benefits_cards}}", benefits_cards)
    file_content = file_content.replace("{{for_whom_elements}}", for_whom_elements)
    file_content = file_content.replace("{{included_elements}}", included_elements)
    file_content = file_content.replace("{{faq_elements}}", faq_elements)
    
    # Structured Data
    file_content = file_content.replace("{{faq_json_ld}}", faq_json_ld)
    file_content = file_content.replace("{{software_app_json_ld}}", software_app_json_ld)
    
    # Write file
    file_path = os.path.join(output_dir, agent["filename"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)
        
    print(f"Generated: {agent['filename']}")
