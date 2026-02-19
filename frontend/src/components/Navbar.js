import { Link } from "react-router-dom";

export default function Navbar() {
  const role = localStorage.getItem("role");

  return (
    <nav style={{ padding: "10px", background: "#f4f4f4" }}>
      
      {/* ✅ Home Link */}
      <Link to="/" style={{ marginRight: "15px" }}>
        Home
      </Link>

      {!role && (
        <>
          <Link to="/login" style={{ marginRight: "15px" }}>
            Login
          </Link>
          <Link to="/register">Register</Link>
        </>
      )}

      {role === "candidate" && (
        <>
          <Link to="/jobs" style={{ marginRight: "15px" }}>
            Jobs
          </Link>
          <Link to="/applications">My Applications</Link>
        </>
      )}

      {role === "recruiter" && (
        <>
          <Link to="/recruiter/dashboard">
            Dashboard
          </Link>
        </>
      )}
    </nav>
  );
}


