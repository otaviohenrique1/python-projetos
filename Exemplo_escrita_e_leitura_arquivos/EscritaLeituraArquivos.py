# Exemplo leitira e escrita de arquivos no python
arquivo = open("ArquivoTexto.txt", "w"); # Abre o arquivo, w -> write
arquivo.write("Banana\n");
arquivo.write("Maca\n");
arquivo.write("Limao\n");
arquivo.write("Laranja\n");
arquivo.write("Abacaxi\n");
arquivo.write("Pera\n");
arquivo = open("ArquivoTexto.txt", "r");
for linha in arquivo:
    print(linha);
print(arquivo.read());
arquivo.close();