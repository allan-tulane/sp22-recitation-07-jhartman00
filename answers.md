# CMPS 2200 Recitation 7
## Answers

**Name:**Jamie Hartman


Place all written answers from `recitation-07.md` here for easier grading.



- **d.**

| File         |   Fixed-Length Coding |   Huffman Coding |   Huffman vs. Fixed-Length |
|--------------|-----------------------|------------------|----------------------------|
| alice29.txt  |               1039367 |           676374 |                0.650755700 |
| asyoulik.txt |                876253 |           606448 |                0.692092352 |
| f1.txt       |                  1340 |              826 |                0.616417910 |
| grammar.lsp  |                 26047 |            17356 |                0.666333935 |
| fields.c     |                 78050 |            56206 |                0.720128123 |

The trend is that compared to the Fixed-Length Coding, Huffman Coding is the better compression algorithm.

- **e.**
  When each character has the same frequency, the huffman coding cost ends up approximately equal to fixed length coding.  Because of this you can use the formula Log_2(n) * num-chars = bit cost.  N in this case is the amount of characters in the alphabet.  This is consistent across documents that have equal character frequency.



