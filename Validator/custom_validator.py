class CustomValidator:
    def __init__(self, rules):
        self.rules = rules
    
    def valider_ligne(self, ligne):
        """Valide une ligne de données selon les règles définies"""
        erreurs = {}
        
        for champ, regle in self.rules.items():
            # Vérifier si le champ est requis
            if 'required' in regle and (champ not in ligne or ligne[champ] is None or str(ligne.get(champ, '')).strip() == ''):
                erreurs[champ] = f"Le champ {champ} est requis"
                continue
            
            # Si le champ n'est pas dans la ligne et n'est pas requis, on passe
            if champ not in ligne or ligne[champ] is None:
                continue
                
            valeur = ligne[champ]
            
            # Vérification numérique
            if 'numeric' in regle and not str(valeur).replace('.', '', 1).isdigit():
                erreurs[champ] = f"Le champ {champ} doit être numérique"
            
            # Vérification string
            if 'string' in regle and not isinstance(valeur, str):
                erreurs[champ] = f"Le champ {champ} doit être une chaîne de caractères"
            
            # Vérification date
            if 'date' in regle:
                import re
                if not re.match(r'^\d{2}/\d{2}/\d{4}$', str(valeur)):
                    erreurs[champ] = f"Le champ {champ} doit être au format JJ/MM/AAAA"
            
            # Vérification between:min,max
            if 'between:' in regle:
                entre_regle = [r for r in regle.split('|') if r.startswith('between:')][0]
                min_val, max_val = entre_regle.replace('between:', '').split(',')
                try:
                    val_num = float(valeur)
                    if val_num < float(min_val) or val_num > float(max_val):
                        erreurs[champ] = f"Le champ {champ} doit être entre {min_val} et {max_val}"
                except ValueError:
                    erreurs[champ] = f"Le champ {champ} doit être un nombre valide pour la vérification between"
        
        return erreurs
    
    def formater_date(self, date_str):
        """Formate une date au format JJ/MM/AAAA"""
        # Vous pouvez améliorer cette fonction selon vos besoins
        return date_str
    
    def formater_classe(self, classe_str):
        """Formate une classe selon vos règles"""
        # Vous pouvez améliorer cette fonction selon vos besoins
        return classe_str