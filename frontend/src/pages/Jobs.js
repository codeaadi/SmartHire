import React, { useEffect, useState } from "react";
import api from "../api/api";

function Jobs() {
  const [jobs, setJobs] = useState([]);
  const [appliedJobs, setAppliedJobs] = useState([]);

  useEffect(() => {
    api
      .get("jobs")
      .then((res) => setJobs(res.data))
      .catch((err) => console.error(err));

    api
    .get("applications/")
    .then((res) => {
      const ids = res.data.map((app) => app.job);
      setAppliedJobs(ids);
    });
  }, []);

  const applyJob = (jobId) => {
    api
      .post("applications/", { job: jobId })
      .then(() => {
        alert("Applied successfully");
        setAppliedJobs(prev=>[...prev, jobId]);
      })
      .catch((err) => {
        console.log(err.response.data);
        alert("Application failed");
      });
  };

  return (
    <>
      <h2>Available Jobs</h2>

      {jobs.map((job) => (
        <div
          key={job.id}
          style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}
        >
          <h3>{job.title}</h3>
          <p>{job.location}</p>
          {appliedJobs.includes(job.id) ? (
            <button disabled>Applied</button>
          ) : (
            <button onClick={() => applyJob(job.id)}>Apply</button>
          )}
        </div>
      ))}
    </>
  );
}

export default Jobs;
