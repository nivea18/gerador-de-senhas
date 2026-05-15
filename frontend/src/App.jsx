import { useState } from 'react';
import axios from 'axios'; // conectar o python
import './App.css'; // import do cdd

function App() {
  
  const [senha, setSenha] = useState("SuaSenhaAqui");

  return (
    <div className="container-gerador">

      <h1 className="titulo-principal">Gerador de Senhas</h1>

      <p className="descricao">
        Gere senhas seguras para o usuário.
      </p>

      <hr className="divisor" />

      <h2 className="subtitulo">Configurações</h2>

      <div className="campo-grupo">
        <label className="label-config">Tamanho da senha:</label>
        <input
          type="number"
          className="input-numero"
          placeholder="Mínimo 6 e máximo 8"
        />
      </div>

      <div className="opcoes-grupo">
        <label className="checkbox-label">
          <input type="checkbox" className="checkbox-input" />
          Incluir letras maiúsculas
        </label>

        <label className="checkbox-label">
          <input type="checkbox" className="checkbox-input" />
          Incluir números
        </label>

        <label className="checkbox-label">
          <input type="checkbox" className="checkbox-input" />
          Incluir caracteres especiais
        </label>
      </div>

      <button className="botao-gerar">
        Gerar Senha
      </button>

      <hr className="divisor" />

      <h2 className="subtitulo">Senha Gerada</h2>

      <div className="resultado-container">
        <input
          type="text"
          className="input-resultado"
          value={senha} 
          readOnly
        />
      </div>

    </div>
  );
}

export default App;