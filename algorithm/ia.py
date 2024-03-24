from math import inf
from entity.pion import Pion
from entity.terrain import Terrain


class IA:
    
    @staticmethod
    def minimax(etat: Terrain, depth, isMax):
        if depth == 0 or etat.isTerminal() :
            return etat.getEvaluation()

        if isMax:
            v = -inf
            for m in etat.nextMove():
                eval_value= IA.minimax(m, depth - 1, False)
                if eval_value > v:
                    v = eval_value
            return v

        else:
            v = +inf
            for m in etat.nextMove():
                eval_value= IA.minimax(m, depth - 1, True)
                if eval_value < v:
                    v = eval_value
            return v
        
    @staticmethod
    def chooseMove(lsPts,lsPolice, voleur):
        best_police = None
        best_move = None
        best_evaluation = -inf
        
        for police in lsPolice:
            for move in police.getPoint().getValidNeighbors(lsPolice,voleur):
                # Créer un nouveau terrain pour simuler le prochain mouvement de la police
                new_ls_police = lsPolice.copy()
                new_police = Pion(police.getX(), police.getY(), move, False)
                new_police.move(move)
                new_ls_police.remove(police)
                new_ls_police.append(new_police)
                print(len(new_ls_police))
                terrain = Terrain(lsPts, False, voleur, new_ls_police)
                
                # Utiliser l'algorithme Minimax pour évaluer ce mouvement
                evaluation= IA.minimax(terrain, depth=3, isMax=True)
                
                # Mettre à jour si l'évaluation est meilleure que celle précédente
                if evaluation > best_evaluation:
                    best_evaluation = evaluation
                    best_police = police
                    best_move = move
        
        return best_police, best_move
    



        

        
        
    
