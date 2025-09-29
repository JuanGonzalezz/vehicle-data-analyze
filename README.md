# Vehicle Data Analyze (Streamlit)

> 🇧🇷 **Resumo:** App simples em **Streamlit** para explorar um dataset de anúncios de veículos (*vehicles.csv*), com **histograma** do odômetro e **dispersão** preço × odômetro. Usa **pandas** + **plotly**. Inclui persistência com `st.session_state` para manter vários gráficos abertos e auto‑reload ao salvar no VS Code.
>
> 🇺🇸 **Summary:** A lightweight **Streamlit** app to explore a vehicle ads dataset (*vehicles.csv*), showing **odometer histogram** and **price vs odometer scatter** using **pandas** + **plotly**. Includes `st.session_state` so multiple charts stay visible and run‑on‑save in VS Code.

---

## ✨ Features

* 🔎 **Exploração rápida** do dataset `vehicles.csv`.
* 📊 **Histograma** de `odometer`.
* 🟣 **Gráfico de dispersão** `odometer` × `price`.
* 🧠 **Estado persistente** com `st.session_state` para manter vários gráficos abertos.
* ♻️ **Auto‑reload** no VS Code (ao salvar) com `.streamlit/config.toml`.

---

## 📦 Requisitos

* **Python** 3.9+
* Bibliotecas: `streamlit`, `pandas`, `plotly`

Você pode instalar via `requirements.txt` (recomendado) ou diretamente com `pip`.

**requirements.txt (sugestão)**

**Deploy**
Available at: https://vehicle-data-analyze.onrender.com

```txt
streamlit>=1.37
pandas>=2.2
plotly>=5.24
```

---

## 🚀 Como rodar (macOS / VS Code)

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/JuanGonzalezz/vehicle-data-analyze.git
   cd vehicle-data-analyze
   ```
2. **Criar e ativar o ambiente virtual**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   # ou
   pip install streamlit pandas plotly
   ```
4. **(Opcional) Habilitar auto‑reload ao salvar**

   ```bash
   mkdir -p .streamlit
   printf "[server]\nrunOnSave = true\n" > .streamlit/config.toml
   ```
5. **Executar o app**

   ```bash
   # usar o módulo (evita problemas de permissão no zsh)
   python -m streamlit run app.py
   ```

> **VS Code:** certifique-se de selecionar o **Python Interpreter** do `.venv`:
> `⌘⇧P` → *Python: Select Interpreter* → escolha `.venv`.

---

## 📂 Estrutura do projeto

```
.
├── app.py
├── vehicles.csv                # dataset (colunas esperadas: odometer, price, ...)
├── requirements.txt
├── .streamlit/
│   └── config.toml             # runOnSave = true (opcional)
└── README.md
```

---

## 🧪 Exemplo de código (com estado persistente)

```python
import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv('vehicles.csv')

car_data = load_data()

st.title('Análise de dados de anúncios de vendas de carros')

# Inicializa flags na sessão
if 'show_hist' not in st.session_state:
    st.session_state.show_hist = False
if 'show_scatter' not in st.session_state:
    st.session_state.show_scatter = False

st.subheader('Histograma do Odômetro')
if st.button('Criar gráfico de histograma', key='btn_hist'):
    st.session_state.show_hist = True

if st.session_state.show_hist:
    fig = px.h
```
