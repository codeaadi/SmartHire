import { useState } from "react";
import api from "../api/api";
import { Link, useNavigate} from "react-router-dom";

function Login() {
  const navigate =useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = () => {
    api
      .post("accounts/login/", {
        email: email.trim(),
        password: password,
      })
      .then((res) => {
        localStorage.setItem('role',res.data.role);
        localStorage.setItem("token", res.data.access);
        alert("Login success");
        if(res.data.role=== 'recruiter'){
          navigate('/recruiter/dashboard');
        }else{
          navigate('/jobs');
        }
      })
      .catch((err) => {
  console.log("Backend error:", err.response.data);
  alert("Invalid credentials");
});
  };

  return (
    <>
      <h2>Login</h2>

      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        value={password}
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="button" onClick={login}>Login</button>
      <p>No account? <Link to='/register'>Register</Link></p>
    </>
  );
}
export default Login;
