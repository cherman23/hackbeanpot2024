"client side"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { auth } from 'gapi-client';

export default function login() {
  const handleGoogleLogin = () => {
    // Handle Google login logic here
    // Use the Google Sign-In API to authenticate the user
    
    // Request permissions for YouTube
    // Use the YouTube Data API to access YouTube resources

    const handleGoogleLogin = async () => {
      try {
        // Use the Google Sign-In API to authenticate the user
        

        const googleUser = await auth.getAuthInstance().signIn();

        // Get the user's Google ID token
        const idToken = googleUser.getAuthResponse().id_token;

        // Send the ID token to your server for verification and user creation

        // Request permissions for YouTube
        await googleUser.grant({
          scope: 'https://www.googleapis.com/auth/youtube.force-ssl',
        });

        // Use the YouTube Data API to access YouTube resources
        // You can now make API calls to the YouTube Data API using the user's credentials
      } catch (error) {
        console.error('Google login error:', error);
      }
    };
  }

  return (
    <div className="flex flex-col h-screen bg-gray-800 dark:bg-gray-900">
      <main className="flex flex-1 flex-col items-center justify-center p-4 space-y-4 text-center">
        <div className="space-y-4">
          <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl lg:text-5xl/none text-white dark:text-gray-300">
            LearnFlow
          </h1>
          <p className="text-sm text-gray-500 dark:text-gray-400">Sign up with your email and password below:</p>
        </div>
        <form className="flex flex-col gap-4 max-w-sm w-full">
          <Input placeholder="Email" type="email" />
          <Input placeholder="Password" type="password" />
          {/* <Button type="submit">Login</Button> */}
          <Button className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded" onClick={handleGoogleLogin}>
            Sign Up with Google
          </Button>
        </form>
      </main>
    </div>
  )
}