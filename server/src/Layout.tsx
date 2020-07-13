import React, { useState} from "react";
import ReactGridLayout, { WidthProvider } from "react-grid-layout";
import Header from "./Components/Header";
import Sidebar from "./Components/Sidebar";
import Content from "./Components/Content";
import faker from "faker";
import fact from "./fact.json";

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
  
  //image
  let [Image, setImage] = useState(null);
  
  function uploader(e:any) {
    setImage(e);
    let img = document.createElement('img');
    img.src = e;
  };

  //chart && table
  function filter(json: any) {
    let list = [];
    for (let key in json) {
      if (json.hasOwnProperty(key)) {
        if (key !== "name" && key !== "description") {
          let data = {
            "name": "",
            "value": 0,
          }; 
          data["name"] = key;
          data["value"] = json[key];
          list.push(data);
        }
        }    
    }
    return list;
  }

  let [Name, setName] = useState("Your result of prediction is: Avocado");
  let [List, setList] = useState(filter(fact.find(el => el.name === "Avocado")));
  let val: any[] = [];
  List.forEach(function(element: any) {
    let value = element["value"];
    val.push(value);
  })
  let [Values, setValues] = useState(val);

  function updater(e: any) {
    e = e.replace(/\s+/g,"");
    setName("Your result of prediction is: " + e)
    setList(filter(fact.find(el => el.name === e)));
    let val: any[] = [];
    List.forEach(function(element: any) {
      let value = element["value"];
      val.push(value);
    })
    setValues(val);
  }

  if (SidebarOn) {
    Sidebars = (
      <Sidebar
        className="Sidebar"
        username={faker.name.firstName()}
        avatar={faker.image.avatar()}
        jobtitle={faker.name.jobTitle()}
        upload={uploader}
        update={updater}
        setName={setName}
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
          <Content image={Image} data={List} value={Values} name={Name}/>
        </div>
      </GridLayout>
    </div>
  );
};

export default Layout;
