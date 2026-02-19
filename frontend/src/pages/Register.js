import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";

export default function Register() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    email: "",
    username:"",
    password: "",
    role: "candidate",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const registerUser = async () => {
    try {
      await api.post("accounts/register/", form);
      alert("Registration Success");
      navigate("/login");
    } catch (err) {
      console.log(err.response?.data);
      alert("Registration failed");
    }
  };

  return (
    <>
      <h2>Register</h2>

      <input
        type="email"
        name="email"
        placeholder="Email"
        onChange={handleChange}
      />
      <input 
      name="username" 
      placeholder="Username" 
      onChange={handleChange} />

      <input
        type="password"
        name="password"
        placeholder="Password"
        onChange={handleChange}
      />
      <select name="role" onChange={handleChange}>
        <option value="candidate">Candidate</option>
        <option value="recruiter">Recruiter</option>
      </select>

      <button onClick={registerUser}>Register</button>
    </>
  );
}
