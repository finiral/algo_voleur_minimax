from math import inf
from entity.pion import Pion
from entity.terrain import Terrain


class IA:
    
    @staticmethod
    def minimax(etat: Terrain, depth, isMax):
        if depth == 0 or etat.isTerminal() :
            return etat.getEvaluation()

        if isMax:
            v = float("-inf")
            for m in etat.nextMove():
                v= max(v,float(IA.minimax(m, depth - 1, False)))
            return v

        else:
            v = float("inf")
            for m in etat.nextMove():
                v= min(v,float(IA.minimax(m, depth - 1, True)))
            return v
        
    @staticmethod
    def chooseMove(lsPts,lsPolice, voleur):
        best_police = None
        best_move = None
        best_evaluation = inf
        
        for police in lsPolice:
            for move in police.getPoint().getValidNeighbors(lsPolice,voleur):
                # Créer un nouveau terrain pour simuler le prochain mouvement de la police
                new_ls_police = lsPolice.copy()
                new_police = Pion(move.getX(), move.getY(), move, False)
                new_ls_police.remove(police)
                new_ls_police.append(new_police)
                terrain = Terrain(lsPts, False, voleur, new_ls_police)
                # Utiliser l'algorithme Minimax pour évaluer ce mouvement
                evaluation= IA.minimax(terrain, depth=3, isMax=True)
                
                # Mettre à jour si l'évaluation est meilleure que celle précédente
                if evaluation < best_evaluation:
                    best_evaluation = evaluation
                    best_police = police
                    best_move = move
        
        return best_police, best_move
    



        

        
        
    
