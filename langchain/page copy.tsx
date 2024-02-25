import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function Component() {
  return (
    <div className="flex flex-col h-screen bg-[#3B72F6] dark:bg-gray-900">
      <header className="flex items-center justify-between h-12 px-4 border-b border-gray-100 dark:border-gray-800 dark:border-gray-850">
        <span className="text-lg font-normal text-white dark:text-gray-300">LearnFlow</span>
        <div className="flex gap-4">
          <Button className="text-sm hover:scale-105 text-black dark:text-gray-300" variant="outline">
            Login
          </Button>
          <Button className="text-sm text-white dark:text-gray-300">Sign Up</Button>
        </div>
      </header>
      <main className="flex flex-1 flex-col items-center justify-center p-4 space-y-4 text-center">
        <div className="space-y-4">
          <h1 className="text-5xl font-normal tracking-tighter sm:text-6xl lg:text-7xl/none text-white dark:text-gray-300">
            LearnFlow
          </h1>
          <p className="text-md text-gray-400 dark:text-gray-400">Enter the topic to get started</p>
        </div>
        <form className="flex flex-col gap-4 max-w-sm w-full">
          <Input placeholder="Enter topic" type="text" />
          <Button className="inline-flex items-center justify-center focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background bg-primary hover:bg-primary/90 h-10 py-2 px-4 w-fullpx-4 bg-gradient-to-r from-black to-black hover:from-black hover:to-black text-white text-lg font-bold rounded-lg transition-transform duration-200 hover:scale-110 cursor-pointer" type="submit">Get Started</Button>
        </form>
      </main>
    </div>
  )
}

