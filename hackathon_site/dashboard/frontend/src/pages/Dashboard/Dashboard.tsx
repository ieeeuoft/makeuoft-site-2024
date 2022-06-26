import React, { useEffect } from "react";
import styles from "./Dashboard.module.scss";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import DashCard from "components/dashboard/DashCard/DashCard";
import TeamCard from "components/dashboard/TeamCard/TeamCard";
import {
    PendingTables,
    CheckedOutTables,
    ReturnedTable,
} from "components/dashboard/ItemTable/ItemTable";
import ProductOverview from "components/inventory/ProductOverview/ProductOverview";
import Header from "components/general/Header/Header";
import { cardItems } from "testing/mockData";
import { hackathonName } from "constants.js";
import { useDispatch, useSelector } from "react-redux";
import { getCurrentTeam, isLoadingSelector } from "slices/event/teamSlice";
import { fulfillmentErrorSelector } from "slices/hardware/cartSlice";
import LinearProgress from "@material-ui/core/LinearProgress";
import {
    getTeamOrders,
    hardwareInOrdersSelector,
    orderErrorSelector,
} from "slices/order/orderSlice";
import { getHardwareWithFilters, setFilters } from "slices/hardware/hardwareSlice";
import { getCategories } from "slices/hardware/categorySlice";
import AlertBox from "components/general/AlertBox/AlertBox";

const Dashboard = () => {
    const dispatch = useDispatch();
    const isTeamLoading = useSelector(isLoadingSelector);
    const orderFulfillmentError = useSelector(fulfillmentErrorSelector);
    const fetchOrderError = useSelector(orderErrorSelector);
    const hardwareInOrders = useSelector(hardwareInOrdersSelector);

    useEffect(() => {
        dispatch(getCurrentTeam());
        dispatch(getCategories());
        dispatch(getTeamOrders());
    }, [dispatch]);

    useEffect(() => {
        if (hardwareInOrders) {
            dispatch(setFilters({ hardware_ids: hardwareInOrders }));
            dispatch(getHardwareWithFilters());
        }
    }, [dispatch, hardwareInOrders]);

    return (
        <>
            <Header />
            <ProductOverview showAddToCartButton={false} />
            <div className={styles.dashboard}>
                <Typography variant="h1">{hackathonName} Hardware Dashboard</Typography>
                {isTeamLoading ? (
                    <LinearProgress
                        style={{ width: "100%", marginTop: 25 }}
                        data-testid="team-linear-progress"
                    />
                ) : (
                    <Grid
                        container
                        direction="row"
                        justifyContent="flex-start"
                        alignItems="flex-start"
                        spacing={2}
                        className={styles.dashboardGrid}
                    >
                        <Grid
                            item
                            md={3}
                            sm={4}
                            xs={6}
                            className={styles.dashboardGridItem}
                            key={0}
                            data-testid="team"
                        >
                            <TeamCard handleEditTeam={() => alert("Editing Team")} />
                        </Grid>
                        {cardItems.map(({ title, content }, i) => (
                            <Grid
                                item
                                md={3}
                                sm={4}
                                xs={6}
                                className={styles.dashboardGridItem}
                                key={i + 1}
                            >
                                <DashCard title={title} content={content} />
                            </Grid>
                        ))}
                    </Grid>
                )}
                {orderFulfillmentError && (
                    <AlertBox
                        error={orderFulfillmentError.errors.map(
                            ({ message }) => message
                        )}
                        title={`There were modifications made to order ${orderFulfillmentError.order_id}`}
                    />
                )}
                {fetchOrderError && <AlertBox error={fetchOrderError} />}
                {/* TODO: add back in when incident reports are completed on the frontend */}
                {/* <BrokenTable items={itemsBroken} openReportAlert={openBrokenTable} /> */}
                <PendingTables />
                <CheckedOutTables />
                <ReturnedTable />
            </div>
        </>
    );
};

export default Dashboard;
