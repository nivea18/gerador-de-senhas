function Contato() {
  return (
    <div className="painel-config formulario-contato">
      <h2 className="subtitulo">Fale Conosco</h2>
      <p className="texto-pagina">Tem alguma dúvida ou sugestão? Envie uma mensagem para a nossa equipe.</p>
      
      <div className="campo-grupo">
        <label className="label-config">Seu Nome:</label>
        <input type="text" className="input-numero" placeholder="Digite seu nome" />
      </div>

      <div className="campo-grupo">
        <label className="label-config">Seu E-mail:</label>
        <input type="email" className="input-numero" placeholder="seu@email.com" />
      </div>

      <div className="campo-grupo">
        <label className="label-config">Mensagem:</label>
        <textarea className="input-numero" rows="4" placeholder="Sua mensagem..." style={{ resize: 'none' }}></textarea>
      </div>

      <button className="botao-gerar">Enviar Mensagem</button>
    </div>
  );
}

export default Contato;