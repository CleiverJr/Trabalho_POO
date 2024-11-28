import React, { useState } from 'react'
import './Predict.css';

import { CardGroup } from 'reactstrap';
import Botao from './botao';
import Table from 'react-bootstrap/Table';



function Predict() {

  const [file, setFile] = useState(null);
  const [predictionResult, setPredictionResult] = useState(null);
  const [futureDates, setFutureDates] = useState([]);
  const [futurePredictions, setFuturePredictions] = useState([]);
  const [isCodigo10MilLinhas, setIsCodigo10MilLinhas] = useState(false);

  const [plotUrlMonteCarlo, setPlotUrlMonteCarlo] = useState('');
  
  const [plotUrl, setPlotUrl] = useState('');
  const [plotUrlFilial, setPlotUrlFilial] = useState('');
  const [plotUrlMes, setPlotUrlMes] = useState('');
  const [plotUrlClientes, setPlotUrlClientes] = useState('');
  const [plotUrlPagamento, setPlotUrlPagamento] = useState('');
  const [plotUrlGenero, setPlotUrlGenero] = useState('');

  const handleFileInputChange = (event) => {
    setFile(event.target.files[0])
  }

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file_upload', file);

    try {
      const endpoint = 'http://localhost:8000/uploadfile/'
      const response = await fetch(endpoint, {
        method: "POST",
        body: formData
      });

      if (response.ok) {
        const result = await response.json();
        setPredictionResult(result.result);
        setFutureDates(result.result.future_dates_week);
        setFuturePredictions(result.result.future_pred_week);
        setIsCodigo10MilLinhas(result.isCodigo10MilLinhas);

        setPlotUrlMonteCarlo(`http://localhost:8000/uploads/${result.plot_url_monteCarlo}`);

        setPlotUrl(`http://localhost:8000/uploads/${result.plot_url}`);
        setPlotUrlFilial(`http://localhost:8000/uploads/${result.plot_url_filial}`);
        setPlotUrlMes(`http://localhost:8000/uploads/${result.plot_url_mes}`);
        setPlotUrlClientes(`http://localhost:8000/uploads/${result.plot_url_clientes}`);
        setPlotUrlPagamento(`http://localhost:8000/uploads/${result.plot_url_pagamento}`);
        setPlotUrlGenero(`http://localhost:8000/uploads/${result.plot_url_genero}`);
        console.log("File uploaded")
      }
      else {
        console.error("Failed");
      }

    } catch (error) {
      console.error(error);
    }
  }

  return (
    <CardGroup style={{ display: 'grid', alignItems: 'center', justifyContent: 'center', height: "100%", marginBottom: "2rem", width: "100%" }} >

      <form onSubmit={handleSubmit} style={{ background: 'transparent', justifyContent: "center", alignItems: "center", display: 'flex', flexDirection: "column", width: "100%" }}>
        <label htmlFor="fileInput" className='custom-file-upload'>
          Selecione o Banco de Dados
        </label>
        <input id="fileInput" className='inputArquivo' type='file' onChange={handleFileInputChange} accept='.csv' />
        {file && <span className='fileName'>{file.name}</span>}
        <Botao type='submit' size='sm' className='botao UIButton' style={{ width: '15rem', height: '4rem', fontSize: '1rem', marginTop: '1rem' }}>Analisar</Botao>
      </form>

      {predictionResult && (
        <div className='resultados'>
          <h3>Previsões Futuras</h3>
          <Table className="table-custom">
            <thead>
              <tr>
                {isCodigo10MilLinhas ? (
                  <>
                    <th>Data</th>
                    <th>Vendas Previstas(Produto 1)</th>
                  </>
                ) : (
                  <>
                    <th>Categoria do Produto</th>
                    <th>Vendas Previstas (Próximos 7 Dias)</th>
                  </>
                )}
              </tr>
            </thead>
            <tbody>
              {isCodigo10MilLinhas ? (
                futureDates.map((date, index) => (
                  <tr key={index}>
                    <td>{date}</td>
                    <td>{futurePredictions[index]}</td>
                  </tr>
                ))
              ) : (
                Object.entries(predictionResult).map(([category, data], index) => (
                  <tr key={index}>
                    <td>{category}</td>
                    <td>{data.future_pred_week}</td>
                  </tr>
                ))
              )}
            </tbody>
          </Table>
          {isCodigo10MilLinhas ? (
            <>
            </>
          ) : (
            <>
            {plotUrlMonteCarlo && <img src={plotUrlMonteCarlo} className='monteCarlo' alt='Predição Monte Carlo' />}
            </>
          )}

          <div className='imagens'>
            {plotUrl && <img src={plotUrl} className='grafico' alt="Gráfico de Predição" />}
            {plotUrlGenero && <img src={plotUrlGenero} className='grafico' alt="Gráfico de Tipo de Gênero" />}
            {plotUrlClientes && <img src={plotUrlClientes} className='grafico' alt="Gráfico de Tipo de Clientes" />}
            {plotUrlFilial && <img src={plotUrlFilial} className='grafico' alt="Gráfico Pizza Filial" />}
            {plotUrlMes && <img src={plotUrlMes} className='grafico' alt="Gráfico Pizza Mês" />}
            {plotUrlPagamento && <img src={plotUrlPagamento} className='grafico' alt="Gráfico de Tipo de Pagamento" />}
          </div>
        </div>
      )}
    </CardGroup>
  )
}

export default Predict;
