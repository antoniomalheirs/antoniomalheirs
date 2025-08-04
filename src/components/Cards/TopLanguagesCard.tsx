import { useCurrentFrame } from 'remotion';
import { UserStats } from '../../config';
import { formatBytes } from '../../functions/utils';
import { fadeInAndSlideUp } from '../../functions/animations';

export function TopLanguagesCard({ userStats }: { userStats: UserStats }) {
  const frame = useCurrentFrame();

  return (
    <div
      className="bg-[#282a36] text-[#f8f8f2] rounded-xl p-4 shadow-lg text-white"
      style={fadeInAndSlideUp(frame)}
    >
      <h3 className="text-l font-semibold mb-2 opacity-80">Top Languages</h3>
      <div className="grid grid-cols-2 gap-1">
        {userStats.topLanguages.slice(0, 8).map((lang, index) => (
          <div
            key={lang.languageName}
            className="flex items-center p-2 bg-gray-700 rounded-lg"
            style={fadeInAndSlideUp(frame - (index * 2))}
          >
            <div className={`w-4 h-4 rounded-full mr-2`} style={{ backgroundColor: `hsl(${index * 60}, 70%, 50%)` }}></div>
            <span className="text-xs flex-grow">{lang.languageName}</span>
            <span className="text-xs font-semibold">{formatBytes(lang.value)}</span>
          </div>
        ))}
      </div>
    </div>
  );
  
} 