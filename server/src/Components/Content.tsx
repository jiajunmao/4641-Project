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
  w: 6,
  h: 2.5,
};

let ContentItem2 = {
  title: "header",
  i: "2",
  x: 6,
  y: 0,
  w: 6,
  h: 2.5,
};

let ContentItem3 = {
  title: "header",
  i: "3",
  x: 0,
  y: 2.5,
  w: 12,
  h: 2.5,
};

let ContentContainer = WidthProvider(ReactGridLayout);

let ItemList = [ContentItem1, ContentItem2, ContentItem3];

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
          <img alt="" src={props.image} id="img"></img>
          </div>
        </div>
        <div key="2" className="item">
          <div className="ContentBox box">
          </div>
        </div>
        <div key="3" className="item">
          <div className="ContentBox box">        
            <ResponsiveContainer>
            <BarChart width={730} height={250} data={props.data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="value" fill="#8884d8" />
            </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </ContentContainer>
    </div>
  );
};

export default Content;
