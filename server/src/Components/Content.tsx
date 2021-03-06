import React, { useEffect } from "react";

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
  w: 4,
  h: 2,
};

let ContentItem2 = {
  title: "header",
  i: "2",
  x: 6,
  y: 0,
  w: 8,
  h: 2,
};

let ContentItem3 = {
  title: "header",
  i: "3",
  x: 0,
  y: 2,
  w: 12,
  h: 3,
};



let ItemList = [ContentItem1, ContentItem2, ContentItem3];

let resizeEvent = new Event('resize');

function update() {
  window.dispatchEvent(resizeEvent);
}

let Content = (props: any) => {
  
  let ContentContainer = props.layout;
  
  useEffect(() => {
    update()
   });

  return (
    <div className="ContentContainer box" id="999">
      <ContentContainer layout={ItemList}>
        <div key="1" className="item">
          <div className="ContentBox box">
          <img alt="" src={props.image} id="img" className="img"></img>
          </div>
        </div>
        <div key="2" className="item">
          <div className="ContentBox box table-container">
          <p className="panel-heading">{props.name}</p>
          <table className="table is-fullwidth is-hoverable">   
            <tbody>
              <tr>
                <th>Calories (kJ)</th>
                <td>{props.list[0]}</td>
                <th>Protein (g)</th>
                <td>{props.list[1]}</td>
                <th>TotalFat (g)</th>
                <td>{props.list[2]}</td>
                <th>Carbohydrate</th>
                <td>{props.list[3]}</td>
              </tr>
              <tr>
                <th>Sodium(mg)</th>
                <td>{props.list[4]}</td>
                <th>SaturatedFat</th>
                <td>{props.list[5]}</td>
                <th>Sugar(g)</th>
                <td>{props.list[6]}</td>
                <th>Calcium(mg)</th>
                <td>{props.list[7]}</td>
              </tr>
              <tr>
                <th>Iron(mg)</th>
                <td>{props.list[8]}</td>
                <th>Potassium(mg)</th>
                <td>{props.list[9]}</td>
                <th>VitaminC(mg)</th>
                <td>{props.list[10]}</td>
                <th>VitaminE(mg)</th>
                <td>{props.list[11]}</td>
              </tr>
            </tbody>
          </table>
          </div>
        </div>
        <div key="3" className="item">
          <div className="ContentBox box">        
            <ResponsiveContainer>
            <BarChart data={props.data}>
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
