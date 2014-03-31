# -*- coding: utf-8 -*-

from webservices_flags import *


METODO_WS = {
    WS_NFE_ENVIO_LOTE: {
        u'webservice': u'NfeRecepcao2',
        u'metodo'    : u'nfeRecepcaoLote2',
    },
    WS_NFE_CONSULTA_RECIBO: {
        u'webservice': u'NfeRetRecepcao2',
        u'metodo'    : u'nfeRetRecepcao2',
    },
    WS_NFE_CANCELAMENTO: {
        u'webservice': u'NfeCancelamento2',
        u'metodo'    : u'nfeCancelamentoNF2',
    },

    WS_NFE_EVENTO: {
        u'webservice': u'RecepcaoEvento',
        u'metodo'    : u'nfeRecepcaoEvento',
        },

    WS_NFE_CONSULTA_DESTINATARIO: {
        u'webservice': u'NfeConsultaDest',
        u'metodo'    : u'nfeConsultaDest',
        },
    WS_NFE_DOWNLOAD_XML_DESTINATARIO: {
            u'webservice': u'NfeDownloadNF',
            u'metodo'    : u'nfeDownloadNF',
            },

    WS_NFE_INUTILIZACAO: {
        u'webservice': u'NfeInutilizacao2',
        u'metodo'    : u'nfeInutilizacaoNF2',
    },
    WS_NFE_CONSULTA: {
        u'webservice': u'NfeConsulta2',
        u'metodo'    : u'nfeConsultaNF2',
    },
    WS_NFE_SITUACAO: {
        u'webservice': u'NfeStatusServico2',
        u'metodo'    : u'nfeStatusServicoNF2',
    },
    WS_NFE_CONSULTA_CADASTRO: {
        u'webservice': u'CadConsultaCadastro2',
        u'metodo'    : u'consultaCadastro2',
    }
}

#nfeConsultaNF2
SVRS = {

    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'ws/nfeConsultaDest/nfeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx',
        },

    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'ws/nfeConsultaDest/nfeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx',
        }
}
# https://app.sefaz.es.gov.br/ConsultaCadastroService/CadConsultaCadastro2.asmx #espirto santo
SVAN = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'www.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_EVENTO : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : u'NFeStatusServico2/NFeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hom.nfe.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_EVENTO : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_DOWNLOAD_XML_DESTINATARIO: u'NfeDownloadNF/NfeDownloadNF.asmx',
        WS_NFE_INUTILIZACAO    : u'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : u'NFeStatusServico2/NFeStatusServico2.asmx'
        }
}


#Ambiente Nacional - (AN)
#Serviço	Versão	URL
#RecepcaoEvento	2.00	https://www.nfe.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx
#NfeConsultaDest	2.00	https://www.nfe.fazenda.gov.br/NFeConsultaDest/NFeConsultaDest.asmx
#NfeDownloadNF	2.00	https://www.nfe.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx
#NfeRecepcao	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeRecepcao2/NfeRecepcao2.asmx
#NfeRetRecepcao	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeRetRecepcao2/NfeRetRecepcao2.asmx
#NfeInutilizacao	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeInutilizacao2/NfeInutilizacao2.asmx
#NfeConsultaProtocolo	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx
#NfeStatusServico	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx
#RecepcaoEvento	2.00	https://www.sefazvirtual.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx
#NfeDownloadNF	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx

SCAN = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'www.scan.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'NfeStatusServico2/NfeStatusServico2.asmx'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hom.nfe.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'SCAN/NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'SCAN/NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'SCAN/NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'SCAN/RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'SCAN/NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'SCAN/NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'SCAN/NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'SCAN/NfeStatusServico2/NfeStatusServico2.asmx'
        }
}


#Sefaz Contingência Ambiente Nacional - (SCAN)
#Serviço	Versão	URL
#NfeRecepcao	2.00	https://www.scan.fazenda.gov.br/NfeRecepcao2/NfeRecepcao2.asmx
#NfeRetRecepcao	2.00	https://www.scan.fazenda.gov.br/NfeRetRecepcao2/NfeRetRecepcao2.asmx
#NfeInutilizacao	2.00	https://www.scan.fazenda.gov.br/NfeInutilizacao2/NfeInutilizacao2.asmx
#NfeConsultaProtocolo	2.00	https://www.scan.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx
#NfeStatusServico	2.00	https://www.scan.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx
#RecepcaoEvento	2.00	https://www.scan.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx


DPEC = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'     : u'www.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: u'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: u'SCEConsultaRFB/SCEConsultaRFB.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'     : u'hom.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: u'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: u'SCEConsultaRFB/SCEConsultaRFB.asmx'
    }
}

#UFAM = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'            : u'nfe.sefaz.am.gov.br',
        #WS_NFE_ENVIO_LOTE        : u'ws/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO: u'ws/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO    : u'ws/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO    : u'ws/services/NfeInutilizacao',
        #WS_NFE_CONSULTA        : u'ws/services/NfeConsulta',
        #WS_NFE_SITUACAO        : u'ws/services/NfeStatusServico'
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'            : u'homnfe.sefaz.am.gov.br',
        #WS_NFE_ENVIO_LOTE        : u'ws/services/NfeRecepcao',
        #WS_NFE_CONSULTA_RECIBO: u'ws/services/NfeRetRecepcao',
        #WS_NFE_CANCELAMENTO    : u'ws/services/NfeCancelamento',
        #WS_NFE_INUTILIZACAO    : u'ws/services/NfeInutilizacao',
        #WS_NFE_CONSULTA        : u'ws/services/NfeConsulta',
        #WS_NFE_SITUACAO        : u'ws/services/NfeStatusServico'
        #}
#}

UFAM = {
    # NfeConsultaCadastro	2.00	https://nfe.sefaz.am.gov.br/services2/services/cadconsultacadastro2
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.am.gov.br',
        WS_NFE_ENVIO_LOTE       : u'services2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'services2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'services2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'services2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'services2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'services2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'services2/services/cadconsultacadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'services2/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : u'homnfe.sefaz.am.gov.br',
        WS_NFE_ENVIO_LOTE       : u'services2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'services2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'services2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'services2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'services2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'services2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'services2/services/cadconsultacadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'services2/services/RecepcaoEvento',
        }
}

UFBA = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : u'nfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE       : u'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'webservices/sre/RecepcaoEvento.asmx',
        WS_NFE_INUTILIZACAO     : u'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'webservices/nfenw/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'webservices/nfenw/CadConsultaCadastro2.asmx',
#        WS_NFE_RECEPCAO_EVENTO  : 'webservices/sre/RecepcaoEvento.asmx',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hnfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE      : u'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'webservices/sre/RecepcaoEvento.asmx',
        WS_NFE_INUTILIZACAO    : u'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'webservices/nfenw/NfeStatusServico2.asmx'
        }
}

UFCE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.ce.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/CadConsultaCadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'nfe2/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'              : u'nfeh.sefaz.ce.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/CadConsultaCadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'nfe2/services/RecepcaoEvento',
        }
}

#UFDF = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'             : u'dec.fazenda.df.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe/ServiceRecepcao.asmx',
        #WS_NFE_CONSULTA_RECIBO : u'nfe/ServiceRetRecepcao.asmx',
        #WS_NFE_CANCELAMENTO     : u'nfe/ServiceCancelamento.asmx',
        #WS_NFE_INUTILIZACAO     : u'nfe/ServiceInutilizacao.asmx',
        #WS_NFE_CONSULTA         : u'nfe/ServiceConsulta.asmx',
        #WS_NFE_SITUACAO         : u'nfe/ServiceStatus.asmx',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe/ServiceConsultaCadastro.asmx',
        #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'             : u'homolog.nfe.fazenda.df.gov.br',
        #WS_NFE_ENVIO_LOTE         : u'nfe/ServiceRecepcao.asmx',
        #WS_NFE_CONSULTA_RECIBO : u'nfe/ServiceRetRecepcao.asmx',
        #WS_NFE_CANCELAMENTO     : u'nfe/ServiceCancelamento.asmx',
        #WS_NFE_INUTILIZACAO     : u'nfe/ServiceInutilizacao.asmx',
        #WS_NFE_CONSULTA         : u'nfe/ServiceConsulta.asmx',
        #WS_NFE_SITUACAO         : u'nfe/ServiceStatus.asmx',
        #WS_NFE_CONSULTA_CADASTRO: u'nfe/ServiceConsultaCadastro.asmx'
        #}
#}

UFGO = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/services/v2/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe/services/v2/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/services/v2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe/services/v2/CadConsultaCadastro2?wsdl',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homolog.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/services/v2/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe/services/v2/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/services/v2/NfeStatusServico2',
        }
}

UFMT = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfews/v2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfews/v2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfews/v2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfews/v2/services/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfews/v2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfews/v2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfews/v2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfews/v2/services/CadConsultaCadastro2?wsdl'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfews/v2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfews/v2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfews/v2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfews/v2/services/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfews/v2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfews/v2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfews/v2/services/NfeStatusServico2',
        #WS_NFE_CONSULTA_CADASTRO: u'nfews/CadConsultaCadastro'
        }
}

UFMS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.fazenda.ms.gov.br',
        WS_NFE_ENVIO_LOTE       : u'producao/services2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'producao/services2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'producao/services2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'producao/services2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'producao/services2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'producao/services2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'producao/services2/CadConsultaCadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'producao/services2/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : u'homologacao.nfe.ms.gov.br',
        WS_NFE_ENVIO_LOTE       :u'homologacao/services2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'homologacao/services2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'homologacao/services2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'homologacao/services2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'homologacao/services2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'homologacao/services2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'homologacao/services2/CadConsultaCadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'homologacao/services2/RecepcaoEvento',
        }
}

UFMG = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe2/services/RecepcaoEvento',
        WS_NFE_CONSULTA_DESTINATARIO : u'nfe2/services/nfeConsultaDest/nfeConsultaDest.asmx',
        WS_NFE_DOWNLOAD_XML_DESTINATARIO: u'nfe2/services/nfeDownloadNF/nfeDownloadNF.asmx',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatus2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/cadconsultacadastro2',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'hnfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe2/services/RecepcaoEvento',
        WS_NFE_CONSULTA_DESTINATARIO : u'nfe2/services/RecepcaoEvento',
        WS_NFE_DOWNLOAD_XML_DESTINATARIO: u'nfe2/services/nfeDownloadNF/nfeDownloadNF.asmx',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatus2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/cadconsultacadastro2',
        }
}

UFPR = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/NFeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe/CadConsultaCadastro2?wsdl',
#        WS_NFE_RECEPCAO_EVENTO  : 'nfe-evento/NFeRecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/NFeStatusServico2'
    }
}

UFPE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.pe.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe-service/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe-service/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe-service/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe-service/services/CadConsultaCadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'nfe-service/services/RecepcaoEvento',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : u'nfehomolog.sefaz.pe.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe-service/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe-service/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe-service/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe-service/services/CadConsultaCadastro2',
#        WS_NFE_RECEPCAO_EVENTO  : 'nfe-service/services/RecepcaoEvento',
    }
}
# https://sef.sefaz.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro2.asmx

UFRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE       : u'ws/Nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'ws/NfeCancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'ws/nfeinutilizacao/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'ws/NfeStatusServico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/cadconsultacadastro/cadconsultacadastro2.asmx',
#        WS_NFE_RECEPCAO_EVENTO  : 'ws/recepcaoevento/recepcaoevento.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : u'homologacao.nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE       : u'ws/Nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'ws/NfeCancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'ws/nfeinutilizacao/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'ws/NfeStatusServico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/cadconsultacadastro/cadconsultacadastro2.asmx',
#        WS_NFE_RECEPCAO_EVENTO  : 'ws/recepcaoevento/recepcaoevento.asmx',
    }
}

#UFRO = {
    #NFE_AMBIENTE_PRODUCAO: {
        #u'servidor'             : u'ws.nfe.sefin.ro.gov.br',
        #WS_NFE_ENVIO_LOTE         : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_ENVIO_LOTE],
        #WS_NFE_CONSULTA_RECIBO : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_CONSULTA_RECIBO],
        #WS_NFE_CANCELAMENTO     : u'wsprod/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : SVRS[NFE_AMBIENTE_PRODUCAO][WS_NFE_INUTILIZACAO],
        #WS_NFE_CONSULTA         : u'wsprod/NfeConsulta',
        #WS_NFE_SITUACAO         : u'wsprod/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'wsprod/CadConsultaCadastro'
    #},
    #NFE_AMBIENTE_HOMOLOGACAO: {
        #u'servidor'             : u'ws.nfe.sefin.ro.gov.br',
        #WS_NFE_ENVIO_LOTE         : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_ENVIO_LOTE],
        #WS_NFE_CONSULTA_RECIBO : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_CONSULTA_RECIBO],
        #WS_NFE_CANCELAMENTO     : u'ws/NfeCancelamento',
        #WS_NFE_INUTILIZACAO     : SVRS[NFE_AMBIENTE_HOMOLOGACAO][WS_NFE_INUTILIZACAO],
        #WS_NFE_CONSULTA         : u'ws/NfeConsulta',
        #WS_NFE_SITUACAO         : u'ws/NfeStatusServico',
        #WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro'
    #}
#}

UFSP = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'              : u'nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : u'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'nfeweb/services/cadconsultacadastro2.asmx',
#        WS_NFE_RECEPCAO_EVENTO  : 'eventosWEB/services/RecepcaoEvento.asmx',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : u'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'nfeweb/services/cadconsultacadastro2.asmx'
        }
}

#
# Informação obtida em
# http://www.nfe.fazenda.gov.br/portal/VerificacaoDeServicos/VerificacaoServicos.aspx
#  Última verificação: 07/04/2010 16:30:14
#  * Estados Emissores pela Sefaz Virtual RS (Rio Grande do Sul): AC, AL, AM, AP, DF, MS, PB, RJ, RO, RR, SC, SE e TO.
#  ** Estados Emissores pela Sefaz Virtual AN (Ambiente Nacional): CE, ES, MA, PA, PI e RN.
# Estados que têm seus próprios servidores: BA, GO, MG, MT, PE, PR, SP.
#


# UF que utilizam a SVAN - Sefaz Virtual do Ambiente Nacional: ES, MA, PA, PI
# UF que utilizam a SVRS - Sefaz Virtual do RS: - Para serviço de Consulta Cadastro: AC, RN, PB, SC
# - Para demais serviços relacionados com o sistema da NF-e: AC, AL, AP, DF, PB, RJ, RN, RO, RR, SC, SE, TO
# Autorizadores: AM BA CE ES GO MG MS MT PE PR RS SP SVAN SVRS SCAN AN

ESTADO_WS = {
    u'AC': SVRS,
    u'AL': SVRS,
    u'AM': UFAM,
    u'AP': SVRS,
    u'BA': UFBA,
    u'CE': UFCE,
    u'DF': SVRS,
    u'ES': SVAN,
    u'GO': UFGO,
    u'MA': SVAN,
    u'MG': UFMG,
#    u'MG': SVAN,
    u'MS': SVRS,
    u'MT': UFMT,
    u'PA': SVAN,
    u'PB': SVRS,
    u'PE': UFPE,
    u'PI': SVAN,
    u'PR': UFPR,
    u'RJ': SVRS,
    u'RN': SVAN,
    u'RO': SVRS,
    u'RR': SVRS,
    u'RS': UFRS,
    u'SC': SVRS,
    u'SE': SVRS,
    u'SP': UFSP,
    u'TO': SVRS
}
