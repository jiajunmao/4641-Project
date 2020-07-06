import React, { useEffect } from "react";
import ReactGridLayout, {WidthProvider } from "react-grid-layout";
import {
  BarChart,
  Bar,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

interface ContentItem {
  title: String;
  i: number;
  x: number;
  y: number;
  w: number;
  h: number;
}

interface ItemList {
  items: ContentItem[];
}

let ContentItem1 = {
  title: "header",
  i: "1",
  x: 0,
  y: 0,
  w: 2,
  h: 2,
};

let ContentItem2 = {
  title: "header",
  i: "2",
  x: 0,
  y: 0,
  w: 2,
  h: 2,
};

let data = [
  {
    name: "Page A",
    uv: 4000,
    pv: 2400,
  },
  {
    name: "Page B",
    uv: 3000,
    pv: 1398,
  },
  {
    name: "Page C",
    uv: 2000,
    pv: 9800,
  },
  {
    name: "Page D",
    uv: 2780,
    pv: 3908,
  },
  {
    name: "Page E",
    uv: 1890,
    pv: 4800,
  },
  {
    name: "Page F",
    uv: 2390,
    pv: 3800,
  },
  {
    name: "Page G",
    uv: 3490,
    pv: 4300,
  },
];

let ContentContainer = WidthProvider(ReactGridLayout);

let ItemList = [ContentItem1, ContentItem2];

let Content = (props: any) => {
  let resizeEvent = new Event('resize');

  function update() {
    window.dispatchEvent(resizeEvent);
  }

  useEffect(() => {
    update()
   });

  return (
    <div className="ContentContainer box" id="999">
      <ContentContainer layout={ItemList}>
        <div key="1" className="item">
          <div className="ContentBox box">
          <ResponsiveContainer>
            <BarChart width={730} height={250} data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="pv" fill="#8884d8" />
              <Bar dataKey="uv" fill="#82ca9d" />
            </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
        <div key="2" className="item">
          <div className="ContentBox box">
            <img alt="" src={props.image} id="img"></img>
          </div>
        </div>
      </ContentContainer>
    </div>
  );
};

export default Content;
