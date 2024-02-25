
"use client"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useRouter } from 'next/navigation';
import { useState, ChangeEvent, FormEvent, useEffect } from 'react';
import Image from 'next/image'
import React from 'react';
// import { PackageIcon } from "@/components/ui/icons";


export default function Component() {
  const [topic, setTopic] = React.useState('');

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append('text', topic);

        try {
            const response = await fetch('http://127.0.0.1:8000/input', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Failed to submit form');
            }

            const responseData = await response.json();
            console.log(responseData);

            // Handle success, e.g., show a success message or redirect
        } catch (error) {
            console.error(error);
            // Handle error, e.g., show an error message
        }
    };

      const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
        setTopic(event.target.value);
      };

      const [loading, setLoading] = useState(true);
  useEffect(() => {
    const timeout = setTimeout(() => {
      setLoading(false);
    }, 1100);

    return () => clearTimeout(timeout);
  }, []);

  const [searchResults, setSearchResults] = React.useState<any[]>([]);

  const handleSubmitForm = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const formData = new FormData(event.target as HTMLFormElement);
    const response = await fetch('http://127.0.0.1:8000/input', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();
    setSearchResults(data.result);
  };

  return (
    <div className="flex flex-col h-screen bg-[#3B72F6] dark:bg-gray-900">
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
        <header className="flex items-center justify-between h-16 px-4 border-b bg-blue-500 md:px-6">
          <div className="flex items-center gap-4">
        <Link className="flex items-center gap-2 text-white" href="#">
          <PackageIcon className="h-6 w-6" />
          <span className="font-semibold">LearnFlow</span>
        </Link>
      </div>
      <nav className="flex items-center space-x-4 text-white dark:text-gray-200">
        <Link className="font-medium" href="/">
          Home
        </Link>
        <Link className="font-medium" href="/pricing">
          Pricing
        </Link>
        <Link className="font-medium" href="/login">
          Login
        </Link>
        <Link
          className="font-medium border border-gray-800 dark:border-gray-200 rounded-lg px-4 py-2 text-sm hover:bg-gray-900/70 bg-gray-900 text-white dark:hover:bg-gray-200 dark:text-gray-800"
          href="/signup"
        >
          Sign Up
        </Link>
      </nav>
        </header>
      )}
      {!loading && (
        <main className="flex flex-1 flex-col items-center justify-center p-4 space-y-4 text-center">
          <div className="space-y-4">
            <h1 className="text-5xl font-normal tracking-tighter sm:text-6xl lg:text-7xl/none text-white dark:text-gray-300">
              LearnFlow
            </h1>
            <p className="text-md text-gray-300 dark:text-gray-400">Enter the topic to get started</p>
          </div>
          <form
            className="flex flex-col gap-4 max-w-sm w-full"
            onSubmit={handleSubmit}
        >
            <Input
                name="text"
                placeholder="What would you like to learn today?"
                value={topic}
                type="text"
                onChange={handleInputChange}
            />
            <button
    className={`inline-flex items-center justify-center focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2
                ring-offset-background bg-primary hover:bg-primary/90 h-10 py-2 px-4 w-fullpx-4 bg-gradient-to-r from-black to-black hover:from-black hover:to-black text-white text-lg font-bold rounded-lg transition-transform duration-200 hover:scale-110 cursor-pointer
                ${topic.trim() === '' ? 'disabled:opacity-50 disabled:pointer-events-none' : ''}`}
    type="button"
    disabled={topic.trim() === ''}
    onClick={() => { window.location.href = '/flow'; }}
>
    Get Started
</button>
                <div className="search-results">
              {searchResults.map((result, index) => (
                <div key={index} className="result-item">
                  <h2>{result.level}</h2>
                  <ul>
                    {result.prompts.map((prompt: string, i: number) => (
                      <li key={i}>{prompt}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
        </form>
        </main>
      )}
    </div>
  );
}
    interface PackageIconProps {
      [key: string]: any;
    }
    
    function PackageIcon(props: PackageIconProps) {
      return (
        <svg
          {...props}
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <path d="m7.5 4.27 9 5.15" />
          <path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z" />
          <path d="m3.3 7 8.7 5 8.7-5" />
          <path d="M12 22V12" />
        </svg>
      );
    }
    

    

{/* 
      <header className="flex items-center justify-between h-16 px-4 border-b bg-blue-500 md:px-6">
      import { PackageIcon } from "@/components/ui/icons"; // Import the missing 'PackageIcon' component

      // Rest of the code...
      <div className="flex items-center gap-4">
        <Link className="flex items-center gap-2 text-white" href="#">
          <PackageIcon className="h-6 w-6" />
          <span className="font-semibold">Acme Inc</span>
        </Link>
      </div>
      <nav className="flex items-center space-x-4 text-white">
        <Link className="font-medium" href="#">
          Home
        </Link>
        <Link className="font-medium" href="#">
          Pricing
        </Link>
        <Link className="font-medium" href="#">
          Login
        </Link>
        <Link className="font-medium border border-white rounded-lg px-3 py-1 text-xs hover:bg-opacity-70" href="#">
          Sign Up
        </Link>
      </nav>
    </header> */}

    {/* <span className="text-lg font-normal text-white dark:text-gray-300">LearnFlow</span>
          <div className="flex gap-4">
            <Button
              className="text-sm hover:scale-105 text-black dark:text-gray-300"
              variant="outline"
              onClick={handleClick}
            >
              Login
            </Button>
            <Button
              className="text-sm text-white dark:text-gray-300"
              onClick={handleSignup}
            >
              Sign Up
            </Button>
          </div> */}