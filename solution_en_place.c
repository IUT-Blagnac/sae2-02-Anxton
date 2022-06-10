#include <stdlib.h>
#include <stdio.h>

// écrase caractère à l'indice i en décalant tout vers l'arrière, réduit la taille de la chaine de 1
void supprimer(char* chaine, int i_ecrase) {
    int i = i_ecrase;
    char* p_char;
    while (chaine[i] != '\0')
    {
        printf("%c: %s\n", chaine[i], chaine);

        // chaine[i] = &chaine[i+1];
        p_char = &chaine[i+1];
        printf("p_char value is %c\n", *p_char);
        chaine[i] = *p_char;
        
        printf("allo?");
        i++;
        printf("i++++?");
    }
    
}

char* erase(char* chaine) {
    // ""
    if (chaine[0] == '\0') {
        printf("VIDE");
        return chaine;
    }
    // " "
    if (chaine[0] == ' ' && chaine[1] == '\0') {
        printf("ESPACE TOUT SEUL");
        chaine[0] == '\0';
        return chaine;
    }
    // espace seul au début (" abc")
    if (chaine[0] == ' ' && chaine[1] != ' ') {
        chaine++;
    }
    // milieu
    int i = 0;
    do
    {
        printf("%d: ",i);
        printf("%c\n",chaine[i]);
        // c'est un espace ?
        if (chaine[i] == ' ')
        {
            // si oui,
            // espace après ?
            if (chaine[i+1] != '\0' && chaine[i+1] == ' ')
            {
                i++;
            }
            // espace avant ?
            else if (i > 0 && chaine[i-1] == ' ')
            {
                i++;
            }
            // espace seul !
            else
            {
                printf("suppression de %s pour le rang %d, le caractere %c\n", chaine, i, chaine[i]);
                supprimer(chaine, i);
            }
        }
        // c'est pas un espace
        else
        {
            i++;
        }
        
        
    } while (chaine[i] != '\0');
    
    return chaine;
}