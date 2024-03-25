% Template MATLAB code for visualizing data from a channel as a 2D line
% plot using PLOT function.

% Prior to running this MATLAB code template, assign the channel variables.
% Set 'readChannelID' to the channel ID of the channel to read from. 
% Also, assign the read field ID to 'fieldID1'. 

% TODO - Replace the [] with channel ID to read data from:
readChannelID = [2479227];
% TODO - Replace the [] with the Field ID to read data from:
fieldID1 = [2];

%% Define time %%
endTime = datetime('now', 'TimeZone', 'local'); % Current time
startTime = endTime - hours(5); % 5 hours ago


% Channel Read API Key 
% If your channel is private, then enter the read API
% Key between the '' below: 
readAPIKey = '8H5DWG60X0PMR7RH';

%% Read Data %%

%[data, time] = thingSpeakRead(readChannelID, 'Field', fieldID1, 'NumPoints', 30, 'ReadKey', readAPIKey);
% Read data within the specified time range
[data, time] = thingSpeakRead(readChannelID, 'Field', fieldID1, 'DateRange', [startTime, endTime], 'ReadKey', readAPIKey);


%% Visualize Data %%

plot(time, data);
