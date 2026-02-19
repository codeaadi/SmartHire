import { useEffect, useState } from "react";
import api from "../api/api";

export default function RecruiterDashboard() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    api
      .get("jobs/recruiter/")
      .then((res) => {
        setJobs(res.data);
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Recruiter Dashboard</h2>

      {jobs.length === 0 ? (
        <p>No Jobs Posted Yet</p>
      ) : (
        jobs.map((job) => (
          <div key={job.id} style={{ marginBottom: "15px" }}>
            <h3>{job.title}</h3>
            <p>{job.description}</p>
            <p>Applicants: {job.applicant_count}</p>
          </div>
        ))
      )}
    </div>
  );
}
