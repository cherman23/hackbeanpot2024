"use client"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import Link from "next/link"
import { useRouter } from 'next/navigation';
import { useState, ChangeEvent, FormEvent, useEffect } from 'react';
import Image from 'next/image'

export default function login() {
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const timeout = setTimeout(() => {
      setLoading(false);
    }, 1100);

    return () => clearTimeout(timeout);
  }, []);

  return (
    <div className="flex flex-col h-screen bg-gray-800 dark:bg-gray-900">
      {loading && (
        <main className="flex flex-1 flex-col items-center justify-center p-4 space-y-4 text-center">
          <div className="space-y-4">
          <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl lg:text-5xl/none text-white dark:text-gray-300 animate-pulse">
        LearnFlow
      </h1>
            <p className="text-sm text-gray-500 dark:text-gray-400">Loading...</p>
          </div>
        </main>
      )}
      {!loading && (
        <main className="flex flex-1 flex-col items-center justify-center p-4 space-y-4 text-center">
          <div className="space-y-4">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl lg:text-5xl/none text-white dark:text-gray-300">
              LearnFlow
            </h1>
            <p className="text-sm text-gray-500 dark:text-gray-400">Enter the URL of a YouTube video to get started</p>
          </div>
          <form className="flex flex-col gap-4 max-w-sm w-full">
            <Input placeholder="Email" type="email" />
            <Input placeholder="Password" type="password" />
            <Button type="submit">Login</Button>
            
            <Button className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded" onClick={() => { window.location.href = "/signup" }}>Sign Up</Button>

          </form>
        </main>
      )}
    </div>
  );
}
