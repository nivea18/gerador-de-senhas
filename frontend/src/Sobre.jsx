function Sobre() {
  return (
    <div className="painel-config completo">
      <h2 className="subtitulo">Sobre o Projeto & Segurança</h2>
      <p className="texto-pagina">
        Este gerador foi desenvolvido como projeto acadêmico para ajudar usuários a criarem credenciais robustas contra ataques de força bruta.
      </p>
      <h3 style={{ color: '#38bdf8', marginBottom: '1rem' }}>Dicas para uma senha segura:</h3>
      <ul className="lista-seguranca">
        <li>Nunca use informações pessoais (datas de nascimento, nomes de familiares).</li>
        <li>Misture letras maiúsculas, minúsculas, números e símbolos (ex: @, #, $, %).</li>
        <li>Use um gerenciador de senhas confiável para não precisar anotar em papéis.</li>
      </ul>
    </div>
  );
}

export default Sobre;