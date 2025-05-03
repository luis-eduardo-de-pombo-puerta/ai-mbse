import { useState } from 'react'
import { PhotoIcon } from '@heroicons/react/24/outline'
import axios from 'axios'
import config from './config'

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [previewUrl, setPreviewUrl] = useState<string | null>(null)
  const [analysis, setAnalysis] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      setSelectedFile(file)
      setPreviewUrl(URL.createObjectURL(file))
      setAnalysis(null)
      setError(null)
    }
  }

  // Drag-and-drop handlers
  const handleDragOver = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault()
    event.stopPropagation()
  }

  const handleDrop = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault()
    event.stopPropagation()
    const file = event.dataTransfer.files?.[0]
    if (file) {
      setSelectedFile(file)
      setPreviewUrl(URL.createObjectURL(file))
      setAnalysis(null)
      setError(null)
    }
  }

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!selectedFile) return

    setLoading(true)
    setError(null)

    const formData = new FormData()
    formData.append('file', selectedFile)

    try {
      const response = await axios.post(`${config.apiUrl}/analyze-diagram`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      setAnalysis(response.data.analysis)
    } catch (err: any) {
      // Check for Hugging Face error
      if (err.response && err.response.data && err.response.data.error === 'huggingface') {
        setError('Hugging Face API is currently unavailable or returned an error. Please try again later.');
      } else {
        setError('Error analyzing the diagram. Please try again.')
      }
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <div className="text-center">
          <h1 className="text-3xl font-bold text-gray-900 mb-8">
            SysML Activity Diagram Analyzer
          </h1>
          <p className="text-gray-600 mb-8">
            Upload a SysML Activity Diagram to analyze its system safety aspects relevant to aerospace engineering.
          </p>
        </div>

        <div className="bg-white/80 shadow-lg rounded-xl p-6 border border-blue-900/30 backdrop-blur-sm">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="flex justify-center">
              <div className="w-full max-w-lg">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Upload Diagram
                </label>
                <div
                  className="mt-1 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10"
                  onDragOver={handleDragOver}
                  onDrop={handleDrop}
                >
                  <div className="text-center">
                    <PhotoIcon className="mx-auto h-12 w-12 text-gray-300" aria-hidden="true" />
                    <div className="mt-4 flex text-sm leading-6 text-gray-600">
                      <label
                        htmlFor="file-upload"
                        className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
                      >
                        <span>Upload a file</span>
                        <input
                          id="file-upload"
                          name="file-upload"
                          type="file"
                          className="sr-only"
                          accept="image/*"
                          onChange={handleFileChange}
                        />
                      </label>
                      <p className="pl-1">or drag and drop</p>
                    </div>
                    <p className="text-xs leading-5 text-gray-600">PNG, JPG, GIF up to 10MB</p>
                  </div>
                </div>
              </div>
            </div>

            {previewUrl && (
              <div className="mt-4">
                <img
                  src={previewUrl}
                  alt="Preview"
                  className="max-w-full h-auto rounded-lg shadow-sm"
                />
              </div>
            )}

            <div className="flex justify-center">
              <button
                type="submit"
                disabled={!selectedFile || loading}
                className="rounded-md bg-blue-700 px-4 py-2.5 text-sm font-bold text-white shadow-lg hover:bg-cyan-400 hover:text-blue-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-cyan-400 transition-all duration-200 border border-blue-300/40 drop-shadow-glow disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? 'Analyzing...' : 'Analyze Diagram'}
              </button>
            </div>
          </form>

          {error && (
            <div className="mt-6 p-4 bg-red-50 rounded-md">
              <p className="text-sm text-red-700">{error}</p>
            </div>
          )}

          {analysis && (
            <div className="mt-6">
              <h2 className="text-lg font-medium text-gray-900 mb-2">Analysis Results</h2>
              <div className="bg-gray-50 p-4 rounded-md">
                <p className="text-gray-700 whitespace-pre-wrap">{analysis}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App
