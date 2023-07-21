# Configurações para criação das tabelas do banco de dados
config_table = {
    'cgh_maria_da_luz':{
        'id':['INT','NOT NULL','AUTO_INCREMENT','PRIMARY KEY'],
        'ug01_nivel_agua':['REAL','NOT NULL'],                        # UG01_Leitura.QTA_NivelMontante
        'ug01_nivel_jusante':['INT','NOT NULL'],                      #	QTA_NivelJusante
        'ug01_tensao_fase_A':['INT','NOT NULL'],                      #	UG01_Leitura.REG615_U_FaseAB
        'ug01_tensao_fase_B':['INT','NOT NULL'],                      # UG01_Leitura.REG615_U_FaseBC
        'ug01_tensao_fase_C':['INT','NOT NULL'],                      #	UG01_Leitura.REG615_U_FaseCA
        'ug01_corrente_fase_A':['INT','NOT NULL'],                    # UG01_Leitura.REG615_I_INST_A
        'ug01_corrente_fase_B':['INT','NOT NULL'],                    # UG01_Leitura.REG615_I_INST_A
        'ug01_corrente_fase_C':['INT','NOT NULL'],                    # UG01_Leitura.REG615_I_INST_A
        'ug01_potencia_ativa':['INT','NOT NULL'],                     # UG01_Leitura.REG615_P_INST
        'ug01_potencia_reativa':['INT','NOT NULL'],                   # UG01_Leitura.REG615_Q_INST
        'ug01_potencia_aparente':['INT','NOT NULL'],                  # UG01_Leitura.REG615_S_INST
        'ug01_fp':['REAL','NOT NULL'],                                # UG01_Leitura.REG615_PF_INST
        'ug01_distribuidor':['INT','NOT NULL'],                       # UG01_Leitura.Turbina_PosicaoDistribuidor
        'ug01_pressao_oleo':['INT','NOT NULL'],                       # UG01_Leitura.UHRV_PressaoOleo
        'ug01_Horimetro_Eletrico':['REAL','NOT NULL'],                              # UG01_Setpoint.Horimetro_Eletrico
        'ug01_velocidade':['INT','NOT NULL'],                         # UG01_Leitura.Turbina_Velocidade
        'ug01_acumulador_energia':['INT','NOT NULL'],                 # UG01_Leitura.Gerador_EnergiaFornecidakWh
        'ug01_temp_mancal_gerador':['INT','NOT NULL'],                # UG01_Leitura.MED_750450_AR1_RTD3
        'ug01_temp_mancal_comb_gerador':['INT','NOT NULL'],           # UG01_Leitura.MED_750450_AR1_RTD4
        'ug01_temp_mancal_turbina':['INT','NOT NULL'],                # UG01_Leitura.MED_750450_AR1_RTD1
        'ug01_temp_mancal_comb_turbina':['INT','NOT NULL'],           # UG01_Leitura.MED_750450_AR1_RTD2
        'ug01_pressao_jusante':['INT','NOT NULL'],                    # UG01_Leitura.Turbina_PressaoJusante
        'ug01_status':['INT','NOT NULL'],                             # UG01_Status.RegV_TurbinaParada
        'data_hora':['TIMESTAMP','NULL','DEFAULT','CURRENT_TIMESTAMP'],
    },
}