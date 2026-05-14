function App() {
  return (
    <div>

      <h1>Gerador de Senhas</h1>

      <p>
        Gere senhas seguras para o usuário.
      </p>

      <hr />

      <h2>Configurações</h2>

      <br />

      <label>Tamanho da senha:</label>

      <br /><br />

      <input
        type="number"
        placeholder="Mínimo 6 e máximo 8"
      />

      <br /><br />

      <label>
        <input type="checkbox" />
        Incluir letras maiúsculas
      </label>

      <br /><br />

      <label>
        <input type="checkbox" />
        Incluir números
      </label>

      <br /><br />

      <label>
        <input type="checkbox" />
        Incluir caracteres especiais
      </label>

      <br /><br />

      <button>
        Gerar Senha
      </button>

      <hr />

      <h2>Senha Gerada</h2>

      <br />

      <input
        type="text"
        value="Abc@123"
        readOnly
      />

    </div>
  )
}

export default App
