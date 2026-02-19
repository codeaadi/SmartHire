import { useEffect, useState } from "react";
import api from "../api/api";

function MyApplications() {
  const [applications, setApplications] = useState([]);

  useEffect(() => {
    api
      .get("applications/")
      .then((res) => setApplications(res.data))
      .catch(() => alert("Failed to load Applications"));
  }, []);

  return (
    <>
      <h2>My Applications</h2>

      {applications.map((app) => (
        <div
          key={app.id}
          style={{ border: "1px solid gray", margin: 10, padding: 10 }}
        >
          <h3>{app.job.title}</h3>
          <p>Status:{app.status}</p>
          <p>Applied on:{app.applied_at}</p>
        </div>
      ))}
    </>
  );
}

export default MyApplications;
