import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";
import { useHistory } from "@docusaurus/router";

type FeatureItem = {
  title: string;
  link: string;
  Svg: React.ComponentType<React.ComponentProps<"svg">>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: "入门篇",
    link: "/docs/category/入门篇",
    Svg: require("@site/static/img/undraw_docusaurus_mountain.svg").default,
    description: <>安装并了解 OpenCV-Python 的基本使用方法。</>,
  },
  {
    title: "基础篇",
    link: "/docs/category/基础篇",
    Svg: require("@site/static/img/undraw_docusaurus_tree.svg").default,
    description: <>学习 OpenCV-Python 在常见图像处理算法中的实践。</>,
  },
  {
    title: "More...",
    link: "/",
    Svg: require("@site/static/img/undraw_docusaurus_react.svg").default,
    description: <>敬请期待...</>,
  },
];

function Feature({ title, link, Svg, description }: FeatureItem) {
  const history = useHistory();
  return (
    <div
      className={clsx("col col--4") + ` ${styles.featureItem}`}
      onClick={() => history.push(link)}
    >
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
