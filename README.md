**Transformei um experimento artístico de colagem manual com revistas em um processo algorítmico usando Python (Pillow). Meu objetivo foi replicar digitalmente a decomposição e reorganização visual de imagens, criando uma estética fragmentada e rítmica. 🐀**

O que eu fiz!:

- Fatiamento e Reagrupamento: Dividi a imagem em tiras verticais, separei-as em grupos de índices pares e ímpares e as concatenei lateralmente. Depois, repeti o mesmo processo no sentido horizontal, resultando em quatro representações reorganizadas.

- Preservação de Dados: Embora o visual final pareça um mosaico complexo, mantive a integridade total da informação; nenhum pixel foi deletado, apenas reposicionado no espaço.

- Conexão Técnica: Percebi que esse método é análogo à técnica de Space-to-Depth (Pixel Unshuffle), utilizada em Redes Neurais Convolucionais para reorganizar dados sem perda de conteúdo.

- Conclusão: O projeto me permitiu unir o lado criativo ao técnico, transformando uma prática intuitiva em um estudo de manipulação estrutural de imagem. Agora, pretendo evoluir para cortes irregulares e novas permutações algorítmicas.

***📝 Nota sobre o processamento das imagens
Durante a execução do código, os arquivos gerados a partir dos cortes e recombinações da imagem são salvos automaticamente na pasta do projeto. Isso inclui:
- impresas_concatenadasPAR.jpg → concatenação das tiras pares
- impresas_concatenadasIMPAR.jpg → concatenação das tiras ímpares
- impresas_concatenadasFINAL.jpg → junção final das duas concatenações
- linhas_impares.png → recombinação das linhas ímpares
- linhas_pares.png → recombinação das linhas pares
Esses arquivos são criados conforme o script roda, permitindo acompanhar cada etapa do processo de manipulação da imagem.
Como usar seu próprio arquivo
Para aplicar o mesmo processo em outra imagem:
- Coloque sua imagem na pasta do projeto.
- No código, altere a linha:
img = Image.open("teste_pil.jpg")
- substituindo "teste_pil.jpg" pelo nome do seu arquivo (ex.: "minha_foto.png").
- Execute o script novamente.
- Os novos resultados serão salvos automaticamente com os mesmos nomes de saída, substituindo os anteriores.***
