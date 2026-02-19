import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function Home() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    const role = localStorage.getItem("role");

    if (token) {
      if (role === "recruiter") {
        navigate("/recruiter/dashboard");
      } else {
        navigate("/jobs");
      }
    }
  }, [navigate]);

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>Welcome to SmartHire</h1>
      <p style={{ fontSize: "18px", marginTop: "10px" }}>
        Connecting top talent with top companies.
      </p>

      <div style={{ marginTop: "40px" }}>
        <button
          style={{ padding: "10px 20px", marginRight: "20px" }}
          onClick={() => navigate("/register")}
        >
          Join as Candidate
        </button>

        <button
          style={{ padding: "10px 20px" }}
          onClick={() => navigate("/register")}
        >
          Hire Talent
        </button>
      </div>

      <div style={{ marginTop: "30px" }}>
        <button
          style={{ padding: "8px 16px" }}
          onClick={() => navigate("/login")}
        >
          Already Have an Account? Login
        </button>
      </div>
    </div>
  );
}

