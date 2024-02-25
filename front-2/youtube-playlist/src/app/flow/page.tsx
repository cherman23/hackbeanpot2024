"use client"
import React from 'react';
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useRouter } from 'next/navigation';
import { useState, ChangeEvent, FormEvent, useEffect } from 'react';
import Image from 'next/image'

const Page: React.FC = () => {
    const [loading, setLoading] = React.useState(true);
    useEffect(() => {
        const timeout = setTimeout(() => {
          setLoading(false);
        }, 7800);
    
        return () => clearTimeout(timeout);
      }, []);
    return (
        
        <div className="flex flex-col h-screen bg-[#3B72F6] dark:bg-gray-900 justify-center items-center">
            {loading && (
         <main className="flex flex-1 flex-col items-center justify-center p-4 space-y-4 text-center">
         <div className="space-y-4">
             <h1 className="text-5xl font-normal tracking-tighter sm:text-6xl lg:text-7xl/none text-white dark:text-gray-300 animate-pulse-fast">
             LearnFlow
             </h1>
         </div>
         </main>
        
        )}
        {!loading && (
            
            <iframe
                width="560"
                height="315"
                src="https://www.youtube.com/embed/videoseries?list=PLTBn-8BnId4Qu7vJ4irdItrQ-uD8mTL35"
                title="YouTube Playlist"
                frameBorder={0}
                allow="autoplay; encrypted-media"
                allowFullScreen
            ></iframe>
        )}
        </div>
    );
};

export default Page;