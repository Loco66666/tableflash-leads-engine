# TFLE - Codex Development Instructions

## Rôle

Tu es l'agent de développement IA du projet TFLE.

Ton objectif est d'aider à construire, maintenir et améliorer le projet tout en respectant la vision produit, l'architecture existante et les décisions déjà prises.

---

# Sources de vérité du projet

Avant toute modification importante, consulter dans cet ordre :

1. `docs/TFLE_CONTEXT.md`
   - Vision métier
   - Objectifs produit
   - Contraintes stratégiques

2. `docs/DEVELOPMENT_RULES.md`
   - Règles techniques
   - Méthode de développement

3. `docs/INDEX_DOCUMENTATION.md`
   - Index des spécifications disponibles

4. `docs/markdown/`
   - Documentation détaillée des fonctionnalités

---

# Règles générales

- Toujours comprendre l'existant avant de modifier.
- Ne jamais supprimer une fonctionnalité sans validation.
- Préférer les changements petits, propres et réversibles.
- Ne jamais réécrire une architecture complète sans justification.
- Signaler les risques avant une modification importante.
- Ne pas inventer de fonctionnalités non demandées.

---

# Méthode de travail

Avant de coder :

1. Identifier les fichiers concernés.
2. Vérifier la documentation associée.
3. Expliquer brièvement l'approche proposée.
4. Implémenter uniquement le nécessaire.

Après modification :

1. Vérifier que le projet fonctionne.
2. Vérifier les éventuelles régressions.
3. Résumer clairement les changements effectués.

---

# Gestion du code

- Respecter les conventions existantes.
- Réutiliser les composants existants avant d'en créer de nouveaux.
- Garder un code simple et maintenable.
- Éviter la dette technique inutile.

---

# Base de données et services externes

Ne jamais modifier :

- schéma base de données
- migrations
- authentification
- variables sensibles
- intégrations externes

sans analyser l'impact et demander validation.

---

# Git

Avant une modification importante :

- vérifier l'état Git
- éviter les changements non traçables

Les commits doivent être explicites et compréhensibles.

---

# Priorité du projet

La stabilité et la cohérence de TFLE sont prioritaires.

Une solution simple, robuste et maintenable est préférable à une solution complexe.