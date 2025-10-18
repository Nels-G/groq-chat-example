# Groq Chat Example

Un exemple simple et fonctionnel d'utilisation de l'API Groq en Python avec streaming en temps réel.

## 📋 Description

Ce projet démontre comment intégrer l'API Groq dans une application Python pour interagir avec des modèles de langage avancés comme Llama. Il utilise le SDK officiel de Groq et permet d'obtenir des réponses en streaming pour une expérience interactive.

## 🚀 Fonctionnalités

- ✅ Intégration simple avec l'API Groq
- ✅ Streaming des réponses en temps réel
- ✅ Gestion sécurisée des clés API avec `python-dotenv`
- ✅ Configuration facile via fichier `.env`
- ✅ Code commenté et facile à comprendre

## 📁 Structure du projet

```
groq-chat-example/
│
├── .env                 # Fichier de configuration (clé API)
├── .gitignore           # Fichiers à ignorer par Git
├── main.py              # Script principal
├── requirements.txt     # Dépendances Python
└── README.md            # Documentation du projet
```

## 🛠️ Prérequis

- **Python 3.10 ou supérieur**
- **pip** (gestionnaire de paquets Python)
- **Une clé API Groq** (obtenue sur [console.groq.com](https://console.groq.com))

## 📦 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/groq-chat-example.git
cd groq-chat-example
```

### 2. Créer un environnement virtuel (recommandé)

```bash
# Sur Windows
python -m venv venv
venv\Scripts\activate

# Sur macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la clé API

Créez un fichier `.env` à la racine du projet :

```env
GROQ_API_KEY=votre_cle_api_ici
```

> ⚠️ **Important** : Ne partagez jamais votre clé API publiquement !

## 🎥 Démonstration vidéo

[![Voir la démo](https://img.shields.io/badge/▶️_Voir_la_démo-red?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/VOTRE_ID_VIDEO/preview)

> Cliquez sur le badge ci-dessus pour voir une démonstration complète du projet en action.

### Aperçu de la démo

<div align="center">
  <a href="https://drive.google.com/file/d/VOTRE_ID_VIDEO/view">
    <img src="https://drive.google.com/thumbnail?id=VOTRE_ID_VIDEO&sz=w1000" alt="Aperçu vidéo démo" width="600"/>
  </a>
  <br>
  <em>Cliquez sur l'image pour voir la vidéo complète</em>
</div>

## 🎮 Utilisation

### Exécution basique

```bash
python main.py
```

Le script enverra une requête au modèle `llama-3.1-8b-instant` et affichera la réponse en temps réel dans le terminal.

### Exemple de sortie

```
Groq est une plateforme d'infrastructure d'IA spécialisée dans l'accélération 
des modèles de langage. Elle offre des performances exceptionnelles grâce à 
son architecture matérielle optimisée...
```

## ⚙️ Personnalisation

### Modifier le prompt

Dans `main.py`, changez le contenu des messages :

```python
messages=[
    {"role": "system", "content": "Tu es un expert en programmation Python."},
    {"role": "user", "content": "Comment créer une API REST avec FastAPI ?"}
]
```

### Paramètres disponibles

| Paramètre | Description | Valeur par défaut |
|-----------|-------------|-------------------|
| `model` | Modèle à utiliser | `llama-3.1-8b-instant` |
| `temperature` | Créativité (0.0 - 2.0) | `0.7` |
| `max_completion_tokens` | Longueur max de réponse | `256` |
| `stream` | Activer le streaming | `True` |

### Modèles disponibles

- `llama-3.1-8b-instant` - Rapide et efficace
- `llama-3.1-70b-versatile` - Plus puissant
- `mixtral-8x7b-32768` - Contexte étendu

## 🔒 Sécurité

### Bonnes pratiques

1. **Ne jamais commiter le fichier `.env`**
   - Ajoutez-le dans `.gitignore`
   
2. **Ne jamais exposer votre clé API dans le code**
   - Utilisez toujours des variables d'environnement

3. **Régénérer votre clé si elle est compromise**
   - Allez sur [console.groq.com](https://console.groq.com)

### Fichier `.gitignore` recommandé

```gitignore
.env
__pycache__/
*.pyc
venv/
.vscode/
.idea/
```

## 📚 Ressources

- [Documentation officielle Groq](https://console.groq.com/docs)
- [SDK Python Groq](https://github.com/groq/groq-python)
- [Modèles disponibles](https://console.groq.com/docs/models)

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

Nelson Galley- [www.linkedin.com/in/nelson-galley]

Lien du projet : [https://github.com/Nels-G/groq-chat-example/]

---

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !
