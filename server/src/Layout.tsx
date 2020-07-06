import React, { useState } from "react";
import ReactGridLayout, { WidthProvider } from "react-grid-layout";
import Header from "./Components/Header";
import Sidebar from "./Components/Sidebar";
import Content from "./Components/Content";
import faker from "faker";

let layout1 = [
  {
    title: "sidebar",
    i: "0",
    x: 0,
    y: 0.2,
    w: 2,
    h: 23.6,
    static: true,
  },
  {
    title: "header",
    i: "1",
    x: 2.05,
    y: 0.2,
    w: 9.85,
    h: 1.8,
    static: true,
  },
  {
    title: "content",
    i: "2",
    x: 2.05,
    y: 3,
    w: 9.85,
    h: 21.8,
    isDraggable: false,
  },
];

let layout2 = [
  {
    title: "sidebar",
    i: "0",
    x: 0,
    y: 0,
    w: 0,
    h: 0,
    isDraggable: false,
  },
  {
    title: "header",
    i: "1",
    x: 0,
    y: 1.2,
    w: 11.85,
    h: 1.8,
    isDraggable: false,
  },
  {
    title: "content",
    i: "2",
    x: 0,
    y: 3,
    w: 11.85,
    h: 22,
    isDraggable: false,
  },
];

let GridLayout = WidthProvider(ReactGridLayout);

let Layout = () => {
  let [SidebarOn, setSidebar] = useState(true);
  let [layouts, setLayout] = useState(layout1);

  let SidebarToggler = () => {
    if (SidebarOn) {
      setLayout(layout2);
      setSidebar(false);
    } else {
      setLayout(layout1);
      setSidebar(true);
    }
  };

  let Sidebars;

  function upload() {
    console.log("Upload!")
  }

  if (SidebarOn) {
    Sidebars = (
      <Sidebar
        className="Sidebar"
        username={faker.name.firstName()}
        avatar={faker.image.avatar()}
        jobtitle={faker.name.jobTitle()}
        uploader={upload}
      />
    );
  } else {
    Sidebars = "";
  }

  let SidebarButton = (
    <button
      className="SidebarToggler button is-light"
      onClick={() => SidebarToggler()}
    >
      <i className="fas fa-bars"></i>
    </button>
  );

  return (
    <div className="layout">
      <GridLayout
        className="grid box"
        layout={layouts}
        cols={12}
        rowHeight={30}
      >
        <div key="0" className="sidebar">
          {Sidebars}
        </div>
        <div key="1">
          <Header SidebarToggler={SidebarButton} />
        </div>
        <div key="2">
          <Content/>
        </div>
      </GridLayout>
    </div>
  );
};

export default Layout;
