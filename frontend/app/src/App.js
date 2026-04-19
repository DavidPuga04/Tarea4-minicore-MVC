import { useState, useEffect } from "react";
import api from "./services/api";

function App() {
  const [inicio, setInicio] = useState("");
  const [fin, setFin] = useState("");
  const [ventas, setVentas] = useState([]);
  const [resultado, setResultado] = useState(null);

  const [monto, setMonto] = useState("");
  const [fecha, setFecha] = useState("");
  const [vendedor, setVendedor] = useState("");

  const [vendedores, setVendedores] = useState([]);

  // cargar datos

  const cargarVentas = async () => {
    const res = await api.get("ventas/");
    setVentas(res.data);
  };

  const cargarVendedores = async () => {
    const res = await api.get("vendedores/");
    setVendedores(res.data);
  };

 useEffect(() => {
  const inicializar = async () => {
    try {
      await api.get("seed/");
    } catch (e) {
      console.log("Seed ya ejecutado");
    }

    cargarVentas();
    cargarVendedores();
  };

  inicializar();
}, []);

  // Crud

  const crearVenta = async () => {
  await api.post("ventas/crear/", {
    vendedor: vendedor,
    monto: monto,
    fecha: fecha
  });

  setMonto("");
  setFecha("");
  setVendedor("");

  cargarVentas();
};

  const eliminarVenta = async (id) => {
    await api.delete(`ventas/eliminar/${id}/`);
    cargarVentas();
  };

  // comisiones

  const calcular = async () => {
    const res = await api.get(`comisiones/?inicio=${inicio}&fin=${fin}`);
    setResultado(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Comisiones</h1>

      
      <h2>Crear Venta</h2>
      <input
        type="number"
        placeholder="Monto"
        onChange={e => setMonto(e.target.value)}
      />

      <input
        type="date"
        onChange={e => setFecha(e.target.value)}
      />

      <select onChange={e => setVendedor(Number(e.target.value))}>
        <option value="">Seleccione vendedor</option>
        {vendedores.map(v => (
          <option key={v.id} value={v.id}>
            {v.nombre}
          </option>
        ))}
      </select>

      <button onClick={crearVenta}>Agregar</button>

      
      <h2>Ventas</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Vendedor</th>
            <th>Monto</th>
            <th>Fecha</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          {ventas.map(v => (
            <tr key={v.id}>
              <td>{v.vendedor}</td>
              <td>{v.monto}</td>
              <td>{v.fecha}</td>
              <td>
                <button onClick={() => eliminarVenta(v.id)}>
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      
      <h2>Calcular Comisiones</h2>
      <input type="date" onChange={e => setInicio(e.target.value)} />
      <input type="date" onChange={e => setFin(e.target.value)} />
      <button onClick={calcular}>Calcular</button>

      
      {resultado && (
        <div>
          <h3>Total Comisiones: {resultado.total_comisiones}</h3>

          <table border="1">
            <thead>
              <tr>
                <th>Vendedor</th>
                <th>Total Ventas</th>
                <th>Comisiones</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(resultado.resumen).map(([nombre, data]) => (
                <tr key={nombre}>
                  <td>{nombre}</td>
                  <td>{data.ventas}</td>
                  <td>{data.comisiones}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;