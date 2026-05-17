import { useState } from 'react';
import axios from 'axios'; // IMPORTANTE: Importando o Axios para fazer a ponte HTTP
import Sobre from './Sobre.jsx';
import Contato from './Contato.jsx';
import './App.css';

function App() {
  const [senha, setSenha] = useState("SuaSenhaAqui");
  const [paginaAtiva, setPaginaAtiva] = useState('home');

  // opções de gerar senhas
  const [tamanho, setTamanho] = useState(8);
  const [maiusculas, setMaiusculas] = useState(true);
  const [numeros, setNumeros] = useState(true);
  const [especiais, setEspeciais] = useState(false);

  // função que conecta com a API flask ou fastAPI
  const lidarComGerarSenha = async () => {
    try {
      // faz uma requisição POST enviando as opções do body em JSON
      const resposta = await axios.post('http://localhost:5000/gerar-senha', {
        tamanho: Number(tamanho),
        maiusculas: maiusculas,
        numeros: numeros,
        especiais: especiais
      });

      // se o servidor responder com Status 200 ou 201, a senha aparece aqui:
      setSenha(resposta.data.senha_gerada);

    } catch (erros) {
      console.error("Erro na comunicação com a API:", erros);
      
      // avaliação de status codes
      if (erros.response) {
        alert(`Erro do Servidor (${erros.response.status}): ${erros.response.data.mensagem || 'Falha ao gerar'}`);
      } else {
        alert("Não foi possível conectar ao servidor backend. O Flask/FastAPI está ligado?");
      }
    }
  };

  return (
    <div className="container-gerador">
      
      {/* menu de navegação  */}
      <nav className="menu-navegacao">
        <button 
          onClick={() => setPaginaAtiva('home')} 
          className={paginaAtiva === 'home' ? 'btn-nav ativo' : 'btn-nav'}
        >
          Gerador
        </button>
        <button 
          onClick={() => setPaginaAtiva('sobre')} 
          className={paginaAtiva === 'sobre' ? 'btn-nav ativo' : 'btn-nav'}
        >
          Sobre
        </button>
        <button 
          onClick={() => setPaginaAtiva('contato')} 
          className={paginaAtiva === 'contato' ? 'btn-nav ativo' : 'btn-nav'}
        >
          Contato
        </button>
      </nav>

      {/* Cabeçalho do Site */}
      <header className="header-site">
        <h1 className="titulo-principal">Gerador de Senhas</h1>
        <p className="descricao">Crie senhas ultra-seguras instantaneamente para proteger suas contas.</p>
      </header>

      
      {paginaAtiva === 'home' && (
        <main className="corpo-site">
          
          {/* Lado Esquerdo: Configurações */}
          <section className="painel-config">
            <h2 className="subtitulo">Configurações</h2>
            
            <div className="campo-grupo">
              <label className="label-config">Tamanho da senha:</label>
              <input 
                type="number" 
                className="input-numero" 
                value={tamanho}
                onChange={(e) => setTamanho(e.target.value)}
                min="6" 
                max="20" 
              />
            </div>

            <div className="opcoes-grupo">
              <label className="checkbox-label">
                <input 
                  type="checkbox" 
                  className="checkbox-input" 
                  checked={maiusculas}
                  onChange={(e) => setMaiusculas(e.target.checked)}
                />
                <span>Incluir letras maiúsculas</span>
              </label>

              <label className="checkbox-label">
                <input 
                  type="checkbox" 
                  className="checkbox-input" 
                  checked={numeros}
                  onChange={(e) => setNumeros(e.target.checked)}
                />
                <span>Incluir números</span>
              </label>

              <label className="checkbox-label">
                <input 
                  type="checkbox" 
                  className="checkbox-input" 
                  checked={especiais}
                  onChange={(e) => setEspeciais(e.target.checked)}
                />
                <span>Incluir caracteres especiais</span>
              </label>
            </div>

            {/* chama a função HTTP ao clicar */}
            <button onClick={lidarComGerarSenha} className="botao-gerar">
              Gerar Senha
            </button>
          </section>

          {/* resultado */}
          <section className="painel-resultado">
            <h2 className="subtitulo">Senha Gerada</h2>
            <div className="resultado-container">
              <input type="text" className="input-resultado" value={senha} readOnly />
            </div>
          </section>

        </main>
      )}

      {paginaAtiva === 'sobre' && <Sobre />}
      {paginaAtiva === 'contato' && <Contato />}

    </div>
  );
}

export default App;