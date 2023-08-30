# import os

# Funcao para identificar nome dos arquivos nos diretorios
# def nome_arquivos_csv(path):
#     csv_list = []
#     for file in os.listdir(path):
#         if file.endswith('.csv'):
#             csv_list.append(file)
#     return csv_list
#
# path_silver_banks    = '../data/silver/banks'
# path_silver_claims   = '../data/silver/claims'
# path_silver_employee = '../data/silver/employee'

### DATA QUALITY ###
# Configurando os pacotes de qualidade de dados
# import yaml
# import great_expectations as gx
# dq_path = '../data/dq'
# data_context: gx.DataContext = gx.get_context()
# context = gx.get_context()
#
# # Configurando data source -> https://docs.greatexpectations.io/docs/0.15.50/guides/connecting_to_your_data/datasource_configuration/how_to_configure_a_spark_datasource/
# datasource_config: dict =   {
#     "name":"data-engineering-usp",
#     "class_name": "Datasource",
#     "module_name": "great_expectations.datasource",
#     "execution_engine": {
#         "class_name": "SparkDFExecutionEngine",
#         "module_name": "great_expectations.execution_engine",
#     },
#     "data_connectors": {
#         "inferred_data_connector":{
#             "class_name": "InferredAssetFilesystemDataConnector",
#             "base_directory": "../data/silver/banks",
#             "default_regex": {
#                 "pattern": "(.*)\\.csv",
#                 "group_names": ["silver"],
#             },
#             "batch_spec_passthrough": {
#                 "reader_method": "csv",
#                 "reader_options": {
#                     "header": True,
#                     "inferSchema": True,
#                 },
#             },
#         }
#     },
# }
#
# # Validar o data source
# data_context.test_yaml_config(yaml.dump(datasource_config))
#
# # Criação do datacontext
# data_context.add_datasource(**datasource_config)