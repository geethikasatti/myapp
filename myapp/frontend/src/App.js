import React from "react";

function App() {
  const [msg, setMsg] = React.useState("loading...");

  React.useEffect(() => {
    fetch("http://localhost:5000/")
      .then(res => res.json())
      .then(data => setMsg(data.message))
      .catch(() => setMsg("backend not reachable"));
  }, []);

  return (
    <div style={{textAlign: "center", marginTop: "50px"}}>
      <h1>Frontend UI</h1>
      <p>Backend says: {msg}</p>
    </div>
  );
}

export default App;
