# Autou Email Classifier ✉️🤖

Classificador automático de e-mails com sugestão de resposta, usando IA leve e backend em Flask.

---

## 🚀 Funcionalidades

- Classificação de e-mails por categoria (Agendamento, Financeiro, Suporte, etc)
- Geração de resposta educada com IA local via [Ollama](https://ollama.com/)
- Frontend simples em HTML/JS
- Backend leve com Flask + Flask-CORS
- Deploy no [Render](https://render.com/) com integração GitHub

---

## 🧠 Tecnologias

- Python 3.13  
- Flask  
- Ollama (`tinyllama`)  
- Git + GitHub  
- Render (Web Service)

---

## 🛠️ Como rodar localmente

```bash
git clone https://github.com/seu-usuario/autou-email-classifier.git
cd autou-email-classifier
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
python backend/app.py 
```
[Acesse aqui](https://autou-api.rvwtech.com.br)

📦 Deploy
- Backend hospedado no Render
- Frontend servido diretamente pela pasta frontend/
- Integração contínua via GitHub
- - ⚠️ Nota: o tempo de resposta pode variar devido ao cold start do Render (especialmente no plano gratuito). Após a primeira requisição, o sistema responde normalmente.


🎥 Demonstração
Video hospedado no meu canal do YouTube no [link](https://youtu.be/aWvsEIioIqE)

✨ Autor
Rafael V. Wierzba
Desenvolvedor e criador do projeto.
Piracaia, SP — Brasil

📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.

