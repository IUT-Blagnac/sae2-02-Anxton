#include <stdlib.h>
#include <stdio.h>

// écrase caractère à l'indice i en décalant tout vers l'arrière, réduit la taille de la chaine de 1
void supprimer(char* chaine, int i_ecrase, int nb_decalages) {
    int i = i_ecrase;
    while (chaine[i+1] != '\0')
    {
        chaine[i] = chaine[i+1];
        i++;
    }
    chaine[i] = '\0';
    
}

char* erase(char* chaine) {
    if (chaine[0] == '\0') {
        printf("VIDE");
        return chaine;
    }
    if (chaine[0] == ' ' && chaine[1] == '\0') {
        printf("ESPACE TOUT SEUL");
        chaine[0] == '\0';
        return chaine;
    }
    int i = 0;
    do
    {
        if (chaine[i] == ' ')
        {
            if (chaine[i+1] == ' ')
            {
                i++;
            }
        }
        
    } while (chaine[i] != '\0' && chaine[i]);
    
    return chaine;
}