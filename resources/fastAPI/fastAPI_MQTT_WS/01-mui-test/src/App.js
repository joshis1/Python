import React from "react";
import PropTypes from "prop-types";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";

import { Button, makeStyles } from "@material-ui/core";
import styles from "./styles/voipline.module.css";

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}


const useStyles = makeStyles({
  switch_button_advanced: {
    background: "#91D7EA",
  },
  tabpanel: {
    background: "#4D4D4D",
  },
});

function App() {
  const classes = useStyles();

   const [value, setValue] = React.useState(0);

   const handleChange = (event, newValue) => {
     setValue(newValue);
   };
  

  return (
    <div>
      <div className={styles.button_advanced}>
        <Button variant="contained" className={classes.switch_button_advanced}>
          SWITCH TO ADVANCED
        </Button>
      </div>

      <div className={classes.root}>
        <AppBar position="static">
          <Tabs
            value={value}
            onChange={handleChange}
            aria-label="simple tabs example"
            className={classes.tabpanel}
          >
            <Tab
              style={{ textTransform: "none" }}
              label="SIP Config"
              {...a11yProps(0)}
            />
            <Tab
              style={{ textTransform: "none" }}
              label="Features"
              {...a11yProps(1)}
            />
            <Tab
              style={{ textTransform: "none" }}
              label="Dial Plan"
              {...a11yProps(2)}
            />
            <Tab
              style={{ textTransform: "none" }}
              label="Quality of Service"
              {...a11yProps(3)}
            />
            <Tab
              style={{ textTransform: "none" }}
              label="NAT"
              {...a11yProps(4)}
            />
            <Tab
              style={{ textTransform: "none" }}
              label="Voice Features"
              {...a11yProps(5)}
            />
          </Tabs>
        </AppBar>
        <TabPanel value={value} index={0}>
          SIP Config
        </TabPanel>
        <TabPanel value={value} index={1}>
          Features
        </TabPanel>
        <TabPanel value={value} index={2}>
          Dial Plan
        </TabPanel>
        <TabPanel value={value} index={3}>
          Quality of Service
        </TabPanel>
        <TabPanel value={value} index={4}>
          NAT
        </TabPanel>
        <TabPanel value={value} index={5}>
          Voice Features
        </TabPanel>
      </div>
    </div>
  );
}

export default App;
