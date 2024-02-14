import React from "react";
import { useSelector } from "react-redux";
import { isTeamInfoLoadingSelector } from "slices/event/teamDetailSlice";
import { projectDescriptionSelector } from "slices/event/teamSlice";
import styles from "./ProjectDescription.module.scss";
import { LinearProgress, Paper, Typography } from "@material-ui/core";

const ProjectDescriptionDetail = () => {
    const projectDescription = useSelector(projectDescriptionSelector);
    // TODO: move project description redux logic to teamSlice
    const isTeamInfoLoading = useSelector(isTeamInfoLoadingSelector);

    return (
        <div>
            {isTeamInfoLoading ? (
                <LinearProgress data-testid="project-description-linear-progress" />
            ) : (
                <>
                    <Typography variant="h2" gutterBottom>
                        Project Description
                    </Typography>
                    <Paper className={styles.projectDescriptionDetail}>
                        <Typography variant="body1">{projectDescription}</Typography>
                    </Paper>
                </>
            )}
        </div>
    );
};

export default ProjectDescriptionDetail;
