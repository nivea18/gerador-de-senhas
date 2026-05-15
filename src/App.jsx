import { useState } from 'react'
import './App.css'

function App() {

  const [pagina, setPagina] = useState('home')
  const [senha, setSenha] = useState('')
  const [cofres, setCofres] = useState([])
  const [nomeCofre, setNomeCofre] = useState('')
  const [senhasSalvas, setSenhasSalvas] = useState([])

  function gerarSenha() {

    const caracteres =
      'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*!'

    let novaSenha = ''

    for (let i = 0; i < 8; i++) {
      novaSenha += caracteres.charAt(
        Math.floor(Math.random() * caracteres.length)
      )
    }

    setSenha(novaSenha)
  }

  function salvarSenha() {

    if (senha !== '') {
      setSenhasSalvas([...senhasSalvas, senha])
    }
  }

  function criarCofre() {

    if (nomeCofre !== '') {
      setCofres([...cofres, nomeCofre])
      setNomeCofre('')
    }
  }

  return (
    <div>

      <button onClick={() => setPagina('home')}>
        Página Inicial
      </button>

      <button onClick={() => setPagina('login')}>
        Login
      </button>

      <button onClick={() => setPagina('registro')}>
        Registro
      </button>

      <button onClick={() => setPagina('cofres')}>
        Meus Cofres
      </button>

      <hr />

      {/* HOME */}

      {pagina === 'home' && (

        <section>

          <h1>Plataforma de Gerenciamento de Senhas</h1>

          <p>
            Homepage da plataforma.
          </p>

          <ul>
            <li>Gerar senhas</li>
            <li>Salvar senhas</li>
            <li>Criar cofres</li>
          </ul>

        </section>

      )}

      {/* LOGIN */}

      {pagina === 'login' && (

        <section>

          <h1>Login</h1>

          <input
            type="email"
            placeholder="Digite seu email"
          />

          <br /><br />

          <input
            type="password"
            placeholder="Digite sua senha"
          />

          <br /><br />

          <button>
            Entrar
          </button>

        </section>

      )}

      {/* REGISTRO */}

      {pagina === 'registro' && (

        <section>

          <h1>Registro</h1>

          <input
            type="text"
            placeholder="Username"
          />

          <br /><br />

          <input
            type="email"
            placeholder="Email"
          />

          <br /><br />

          <input
            type="password"
            placeholder="Senha"
          />

          <br /><br />

          <input
            type="password"
            placeholder="Confirmar senha"
          />

          <br /><br />

          <button>
            Registrar
          </button>

        </section>

      )}

      {/* COFRES */}

      {pagina === 'cofres' && (

        <section>

          <h1>Meus Cofres</h1>

          <h2>Criar Cofre</h2>

          <input
            type="text"
            placeholder="Nome do cofre"
            value={nomeCofre}
            onChange={(e) => setNomeCofre(e.target.value)}
          />

          <br /><br />

          <button onClick={criarCofre}>
            Criar Cofre
          </button>

          <br /><br />

          <ul>
            {cofres.map((cofre, index) => (
              <li key={index}>{cofre}</li>
            ))}
          </ul>

          <hr />

          <h2>Gerador de Senhas</h2>

          <button onClick={gerarSenha}>
            Gerar Senha
          </button>

          <br /><br />

          <input
            type="text"
            value={senha}
            readOnly
          />

          <br /><br />

          <button onClick={salvarSenha}>
            Salvar Senha
          </button>

          <hr />

          <h2>Senhas Salvas</h2>

          <ul>
            {senhasSalvas.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

        </section>

      )}

    </div>
  )
}

export default App