import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import { styled } from "@stitches/react";
import * as PopoverPrimitive from "@radix-ui/react-popover";
import { Popover, PopoverTrigger, PopoverContent } from "../components/popover";

const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>Eloka Agu</title>
        <meta
          name="description"
          content="Personal portfolio website, built with NextJs and Radix and deployed on Vercel"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1>Hello world</h1>
      </main>
    </div>
  );
};

export default Home;
